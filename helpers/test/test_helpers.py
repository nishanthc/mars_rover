import unittest

from helpers.inputs import parse_map_size


class TestParseMapSize(unittest.TestCase):
    """
    Test cases for the parse_map_size method.
    """

    def test_valid_input(self):
        """
        Tests that when a valid input is provided the map size data is correctly parsed.
        """
        map_size = parse_map_size("2 7")
        self.assertEqual(map_size[0], 2)
        self.assertEqual(map_size[1], 7)

        map_size = parse_map_size("8 4")
        self.assertEqual(map_size[0], 8)
        self.assertEqual(map_size[1], 4)

        map_size = parse_map_size("82 41")
        self.assertEqual(map_size[0], 82)
        self.assertEqual(map_size[1], 41)

    def test_invalid_input(self):
        """
        Tests that when an invalid input is provided the correct exceptions are raised.
        """
        # letters in string
        with self.assertRaises(ValueError):
            parse_map_size("a 7")

        with self.assertRaises(ValueError):
            parse_map_size("9 b")

        # more than 2 numerical values
        with self.assertRaises(ValueError):
            parse_map_size("10 10 10")

        # floats
        with self.assertRaises(ValueError):
            parse_map_size("10.4 15.2")
