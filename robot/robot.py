from helpers.constants import headings
from world.world import World


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

    move(world, commands): Returns if the move was sucessful with either the final position
    or the last possible position.
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
        self.last_valid_position: tuple = None

    def move(self, world: World, commands: list):
        """
        Initializes a new instance of the Robot class with the given x, y and heading.

        Args:
        world (World): An instance of the world that the commands should be performed on.
        commands (list): A list of commands to be performed by the robot.
        """
        pass
