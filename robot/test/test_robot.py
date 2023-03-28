import unittest

from robot.robot import Robot


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
