import unittest

from robot.robot import Robot
from world.world import World


class TestRobot(unittest.TestCase):
    """
    Test cases for the Robot class.
    """

    def test_integer_for_position_heading_correct(self):
        """
        Tests the initialisation of the Robot class with valid input parameters.
        """
        robot = Robot(3, 4, "N")
        self.assertEqual(robot.x, 3)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.heading, "N")

        robot = Robot(6, 2, "W")
        self.assertEqual(robot.x, 6)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.heading, "W")

    def test_init_invalid_input(self):
        """
        Tests the initialization of the Robot class with invalid input parameters.
        """

        # String for width and height
        with self.assertRaises(TypeError):
            Robot("invalid", 4, "S")
        with self.assertRaises(TypeError):
            Robot(4, "invalid", "E")

        # Float for width and height
        with self.assertRaises(TypeError):
            Robot(3, 4.5, "N")
        with self.assertRaises(TypeError):
            Robot(4.5, 3, "W")

        # Invalid headings
        # invalid letter
        with self.assertRaises(ValueError):
            Robot(3, 4, "K")
        # integer provided for heading
        with self.assertRaises(TypeError):
            Robot(4, 4, 3)

    def test_initial_position_check_valid(self):
        """
        Tests the initial_position_check_valid method on the Robot class with valid initial state
         data and World instance.
        """
        # max position
        world = World(width=3, height=4)
        robot = Robot(3, 4, "N")
        self.assertEqual(robot.initial_position_check(world=world), True)

        # inner position
        world = World(width=5, height=5)
        robot = Robot(2, 2, "S")
        self.assertEqual(robot.initial_position_check(world=world), True)

    def test_initial_position_check_out_of_bounds(self):
        """
        Tests the initial_position_check_valid method on the Robot class with an
        invalid initial state (out of bounds) data and World instance.
        """
        # out of bounds extreme high
        world = World(width=3, height=4)
        robot = Robot(5, 5, "N")
        self.assertEqual(robot.initial_position_check(world=world), False)

        # out of bounds extreme low
        world = World(width=5, height=5)
        robot = Robot(-2, 2, "S")
        self.assertEqual(robot.initial_position_check(world=world), False)

    def test_move_valid(self):
        """
        Tests the move method returns the correct position after the commands have been executed
        """
        world = World(width=4, height=4)
        robot = Robot(0, 0, "N")
        on_map, position = robot.move(world=world, commands="FRFRF")
        self.assertEqual(position, (1, 0, "S"))

        robot = Robot(0, 0, "N")
        on_map, position = robot.move(world=world, commands="RFF")
        self.assertEqual(position, (2, 0, "E"))

    def test_move_invalid(self):
        """
        Tests the move method returns the correct position after the commands have been executed
        """
        world = World(width=4, height=4)
        robot = Robot(0, 0, "W")
        on_map, position = robot.move(world=world, commands="F")
        self.assertEqual(on_map, False)
        self.assertEqual(position, (0, 0, "W"))

        robot = Robot(0, 0, "N")
        on_map, position = robot.move(world=world, commands="FFFFF")
        self.assertEqual(on_map, False)
        self.assertEqual(position, (0, 4, "N"))
