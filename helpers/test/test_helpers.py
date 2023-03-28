import unittest

from helpers.inputs import parse_map_size, parse_initial_position_and_commands


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


class TestParseStateCommandsHelper(unittest.TestCase):
    """
    Test cases for the parse_initial_position_and_commands method.
    """

    def test_valid_input(self):
        """
        Tests that when a valid initial position and commands are sent they are correctly
        parsed and returned.
        """

        initial_state, commands = parse_initial_position_and_commands("(2, 3, E) LFRFF")
        self.assertEqual(initial_state, (2, 3, "E"))
        self.assertEqual(commands, ["L", "F", "R", "F", "F"])

        initial_state, commands = parse_initial_position_and_commands(
            "(14, 10, N) FFFFR"
        )
        self.assertEqual(initial_state, (14, 10, "N"))
        self.assertEqual(commands, ["F", "F", "F", "F", "R"])

        initial_state, commands = parse_initial_position_and_commands("(1, 4, S) RLRLR")
        self.assertEqual(initial_state, (1, 4, "S"))
        self.assertEqual(commands, ["R", "L", "R", "L", "R"])

    def test_invalid_position_letter(self):
        """
        Tests that when a letter is included in the positional data a Value Error is returned.
        """

        # incorrect position
        with self.assertRaises(ValueError):
            parse_initial_position_and_commands("(X, 3, E) LFRFF")

    def test_invalid_position_negative(self):
        """
        Tests that when a negative number is included in the positional data a Value Error is returned.
        """
        with self.assertRaises(ValueError):
            parse_initial_position_and_commands("(-1, 3, W) LFRFF")

    def test_invalid_position_heading_unrecognised(self):
        """
        Tests that when a unrecognised heading is included in the positional
        data a Value Error is returned.
        """

        # incorrect heading
        with self.assertRaises(ValueError):
            parse_initial_position_and_commands("(2, 3, F) LFRFF")

    def test_invalid_position_heading_number(self):
        """
        Tests that when a number is used as a heading in the positional data a Value Error is returned.
        """

        with self.assertRaises(ValueError):
            parse_initial_position_and_commands("(2, 3, 1) LFRFF")

    def test_invalid_command_numbers(self):
        """
        Tests that when a number is included in the commands data a Value Error is returned.
        """

        # incorrect commands
        with self.assertRaises(ValueError):
            parse_initial_position_and_commands("(2, 3, W) 1FRFF")

    def test_invalid_unrecognised_commands(self):
        """
        Tests that when unrecognised characters are found in the commands data a Value Error is returned.
        """
        with self.assertRaises(ValueError):
            parse_initial_position_and_commands("(2, 3, W) XXXXX")
