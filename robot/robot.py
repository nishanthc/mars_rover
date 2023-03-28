from helpers.constants import headings


class Robot:
    """
    Represents a robot.

    Attributes:
    x (int): The position of the robot on the X axis.
    y (int): The position of the robot on the Y axis.
    H (str): The heading of the robot.

    Methods:
    __init__(x, y, heading): Initializes a new instance of the Robot class with the given x and y
     positions and heading.
    """

    def __init__(self, x: int, y: int, heading: str):
        """
        Initializes a new instance of the Robot class with the given x, y and heading.

        Args:
        x (int): The position of the robot on the X axis.
        y (int): The position of the robot on the Y axis.
        H (str): The heading of the robot.
        """

        # if x or y are not Integers then a TypeError is raised.
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        # if heading is not a String then return a TypeError.
        if not isinstance(heading, str):
            raise TypeError("heading must be a string")

        # if heading is not either N E S W then raise n ValueError.
        if heading not in headings:
            raise ValueError("heading must either be N E S W")

        self.x: int = x
        self.y: int = y
        self.heading: str = heading
