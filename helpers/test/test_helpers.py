import unittest

from helpers.inputs import parse_map_size, parse_initial_position_and_commands
from helpers.navigation import find_heading_after_turn, find_position_after_forward_move
from world.world import World


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


class TestFindHeading(unittest.TestCase):
    """
    Test cases for the find_heading_after_turn method.
    """

    def test_check_if_valid_heading_returned(self):
        """
        Tests that when a valid input is provided the correct new heading is returned.
        """
        self.assertEquals(find_heading_after_turn(turn="R", current_heading="N"), "E")
        self.assertEquals(find_heading_after_turn(turn="R", current_heading="E"), "S")
        self.assertEquals(find_heading_after_turn(turn="R", current_heading="W"), "N")

        self.assertEquals(find_heading_after_turn(turn="L", current_heading="N"), "W")
        self.assertEquals(find_heading_after_turn(turn="L", current_heading="E"), "N")
        self.assertEquals(find_heading_after_turn(turn="L", current_heading="W"), "S")

    def test_check_if_invalid_command_given(self):
        """
        Tests that when a invalid input the correct error is raised
        """
        with self.assertRaises(ValueError):
            self.assertEquals(
                find_heading_after_turn(turn="A", current_heading="N"), "E"
            )

        with self.assertRaises(ValueError):
            self.assertEquals(
                find_heading_after_turn(turn="R", current_heading="A"), "E"
            )


class TestFindPositionAfterMove(unittest.TestCase):
    """
    Test cases for the find_position_after_forward_move method.
    """

    def test_check_valid_forward_movement(self):
        """
        Tests that when a valid move is presented the corrent new position is returned
        """
        world = World(height=5, width=5)
        self.assertEquals(
            find_position_after_forward_move(x=0, y=0, heading="N", world=world),
            (True, 0, 1, "N"),
        )
        self.assertEquals(
            find_position_after_forward_move(x=1, y=1, heading="E", world=world),
            (True, 2, 1, "E"),
        )
        self.assertEquals(
            find_position_after_forward_move(x=4, y=4, heading="S", world=world),
            (True, 4, 3, "S"),
        )

    def test_check_invalid_forward_movement(self):
        """
        Tests that when an invalid move is presented the corrent new position is returned
        """
        world = World(height=5, width=5)
        self.assertEquals(
            find_position_after_forward_move(x=5, y=5, heading="N", world=world),
            (False, 5, 5, "N"),
        )
        self.assertEquals(
            find_position_after_forward_move(x=0, y=5, heading="W", world=world),
            (False, 0, 5, "W"),
        )
        self.assertEquals(
            find_position_after_forward_move(x=3, y=5, heading="N", world=world),
            (False, 3, 5, "N"),
        )
