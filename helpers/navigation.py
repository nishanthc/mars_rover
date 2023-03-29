from helpers.constants import headings
from world.world import World


def find_heading_after_turn(current_heading: str, turn: str) -> str:
    """
    Given the current heading and the direction of the turn ("R" for right or "L" for left),
    returns the new heading after completing the turn.

    Args:
    current_heading (str): The current heading, represented as a string ("N", "E", "S", or "W").
    turn (str): The direction of the turn ("R" for right or "L" for left).

    Returns:
    str: The new heading after completing the turn, represented as a string ("N", "E", "S", or "W").

    Raises:
    ValueError: If the input `current_heading` is not a valid heading ("N", "E", "S", or "W"),
                or if the input `turn` is not "R" or "L".
    """

    if turn not in ["R", "L"]:
        raise ValueError("Invalid turn: must be one of 'L' or 'R'.")

    if current_heading not in headings:
        raise ValueError(
            "Invalid current_heading: must be one of 'N', 'E', 'S', or 'W'."
        )

    if turn == "R":
        try:
            heading = headings[headings.index(current_heading) + 1]
        except IndexError:
            heading = headings[0]
    if turn == "L":
        try:
            heading = headings[headings.index(current_heading) - 1]
        except IndexError:
            heading = headings[-1]
    return heading


def find_position_after_forward_move(
    x: int, y: int, heading: str, world: World
) -> (bool, int, int, int):
    """
    Given the x, y and heading of a robot return the new position after a forward movement.

    Args:
    x (int): The current position of the robot on the x axis.
    y (int): The current position of the robot on the y axis.

    Returns:
    boolean: success
    int: x axis
    int: y axis
    str: heading



    """

    if heading not in headings:
        raise ValueError(
            "Invalid current_heading: must be one of 'N', 'E', 'S', or 'W'."
        )
    success = True
    if heading == "N":
        y = y + 1
    if heading == "S":
        y = y - 1
    if heading == "E":
        x = x + 1
    if heading == "W":
        x = x - 1

    if x > world.width:
        success = False
        x = x - 1

    if x < 0:
        success = False
        x = x + 1

    if y > world.height:
        success = False
        y = y - 1

    if y < 0:
        success = False
        y = y + 1

    return success, x, y, heading
