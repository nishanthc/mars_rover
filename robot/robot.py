from helpers.constants import headings
from helpers.navigation import find_heading_after_turn, find_position_after_forward_move
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

    def initial_position_check(self, world: World):
        """
        Checks if the starting position of the robot is valid for the world it's being placed on

        Args:
        world (World): An instance of the world that the commands should be performed on.

        :Returns
        boolean: True or False depending on if the check is successful or not

        """
        if (self.x > world.width or self.x < 0) or 0 > (
            self.y > world.height or self.y < 0
        ):
            return False
        else:
            return True

    def move(self, world: World, commands: list):
        """
        Attempts to run the commands for the robot on a given world.

        Args:
        world (World): An instance of the world that the commands should be performed on.
        commands (list): A list of commands to be performed by the robot.

          :Returns
          boolean: success state
          Tuple: The latest position of the robot


        """
        if self.initial_position_check(world=world):
            on_map = True
            for command in commands:
                if on_map:
                    if command in ["L", "R"]:
                        self.heading = find_heading_after_turn(
                            turn=command, current_heading=self.heading
                        )
                    if command == "F":
                        (
                            on_map,
                            self.x,
                            self.y,
                            self.heading,
                        ) = find_position_after_forward_move(
                            x=self.x, y=self.y, heading=self.heading, world=world
                        )
            return on_map, (self.x, self.y, self.heading)

        else:
            raise ValueError("The robot cannot be placed in the world")
