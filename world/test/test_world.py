import unittest

from world.world import World


class TestWorld(unittest.TestCase):
    """
    Test cases for the World class.
    """

    def test_integer_for_height_and_width(self):
        """
        Tests the initialisation of the World class with valid input parameters.
        """
        world = World(3, 4)
        self.assertEqual(world.width, 3)
        self.assertEqual(world.height, 4)

    def test_init_invalid_input(self):
        """
        Tests the initialization of the World class with invalid input parameters.
        """

        # String for width and height
        with self.assertRaises(TypeError):
            World("invalid", 4)
        with self.assertRaises(TypeError):
            World(4, "invalid")

        # Float for width and height
        with self.assertRaises(TypeError):
            World(3, 4.5)
        with self.assertRaises(TypeError):
            World(4.5, 3)
