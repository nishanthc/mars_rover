from typing import List, Tuple


from helpers.constants import headings


def parse_map_size(map_size_string: str) -> List[int]:
    """
    Parses a string and returns an array of integers.

    Args:
        map_size_string (str): A string of integers separated by a space.

    Returns:
        list: An array of integers parsed from the input string.

    Raises:
        ValueError: If the input string cannot be parsed as a valid array of integers.

    Example:
        >>> parse_map_size('2 6')
        [2, 6]
        >>> parse_map_size('1 2 3')
        [1, 2, 3]
    """
    try:
        # Split the input string into separate strings for each integer
        map_size_list = map_size_string.strip().split()

        if len(map_size_list) != 2:
            raise ValueError(
                "The input string must only contain 2 integers seperated by a space"
            )

        # Convert each string into an integer and append to the output list
        map_size_integer_list = [int(x) for x in map_size_list]

        # Return the output list
        return map_size_integer_list
    except ValueError:
        # If the input string cannot be parsed as a valid array of integers, raise a ValueError
        raise ValueError("Input string must contain only integers separated by a space")


def parse_initial_position_and_commands(
    position_and_commands: str,
) -> Tuple[Tuple[int, int, str], List[str]]:
    """
    Parses a string and returns a tuple that represents the initial position of a robot and a
     list of valid commands.

    Args:
        position_and_commands: A string of the form "(x, y, h) moves", where x and y are
        integers, h is a single letter
        representing the heading, and commands is a sequence of characters "F", "L", and "R".

    Returns:
        A tuple containing a position tuple (x, y, h) and a list of valid movements.

    Raises:
        ValueError: If the input string is not in the expected format.

    Example:
        >>> parse_input("(2, 3, E) LFRFF")
        ((2, 3, 'E'), ['L', 'F', 'R', 'F', 'F'])
    """
    try:
        # Split the input string into position tuple and moves list
        position_and_commands = position_and_commands.strip().replace(" ", "")

        # Split the whole input string by ")" and then remove "(" from the first item of the split
        position_string, commands = [
            x[1:] if n == 0 else x
            for n, x in enumerate(position_and_commands.split(")"))
        ]

        x, y, h = position_string.split(",")
        x = int(x)
        y = int(y)
        h = str(h)

        if x < 0 or y < 0:
            raise ValueError("X or Y cannot be less than 0")

        # Parse the position tuple as a tuple of integers and a string
        position_tuple = tuple([x, y, h])

        # check if positions are valid
        if not isinstance(position_tuple[0], int) or not isinstance(
            position_tuple[1], int
        ):
            raise ValueError(
                "The X and Y of the positional input needs to be an integer"
            )

        # check if heading is a valid heading
        if position_tuple[2] not in headings:
            raise ValueError("heading must either be N E S W")

        # Parse the moves list as a list of valid moves
        for command in commands:
            if command not in ["F", "L", "R"]:
                raise ValueError("heading must either be F LR ")

        # Return the position tuple and list of valid moves as a tuple
        return (position_tuple, list(commands))
    except Exception:
        raise ValueError(
            "Input string must be in the format '(x, y, d) moves' with valid moves 'F', 'L', and 'R'"
        )
