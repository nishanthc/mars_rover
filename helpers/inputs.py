from typing import List


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
