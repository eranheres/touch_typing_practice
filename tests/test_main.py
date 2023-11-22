# imports
import unittest
from unittest.mock import MagicMock, patch

from touch_typing_practice.main import main


class TestMainFunction(unittest.TestCase):
    @patch("touch_typing_practice.typing_practice.TypingPractice.get_user_statistics")
    @patch("touch_typing_practice.user.User.load")
    @patch.object(curses.window, "getstr")
    def test_main_user_interaction(
        self, mock_getstr, mock_load, mock_get_user_statistics
    ):
        # Set up the mock objects
        mock_getstr.side_effect = [
            "mocked_username",
            "1",
            "mocked_text",
            "mocked_typed_text",
        ]
        mock_user_instance = MagicMock()
        mock_load.return_value = mock_user_instance
        mock_get_user_statistics.return_value = {
            "mocked_time": {"wpm": 50, "accuracy": 90}
        }

        # Call the main function with a mocked stdscr object
        main(MagicMock())

        # Assertions to verify the behavior of the main function
        mock_load.assert_called_once_with(b"mocked_username")
        mock_get_user_statistics.assert_called_once()
        self.assertEqual(mock_getstr.call_count, 4)

    @patch("touch_typing_practice.typing_practice.TypingPractice.get_user_statistics")
    @patch("touch_typing_practice.user.User.load")
    @patch("curses.window.getstr")
    def test_main_invalid_choice(
        self, mock_getstr, mock_load, mock_get_user_statistics
    ):
        # Set up the mock objects
        mock_getstr.side_effect = [
            b"mocked_username",
            b"invalid_choice",
            b"1",
            b"mocked_text",
            b"mocked_typed_text",
        ]
        mock_load.return_value = MagicMock()
        mock_get_user_statistics.return_value = {
            "mocked_time": {"wpm": 50, "accuracy": 90}
        }
        # Call the main function with a mocked stdscr object
        main(MagicMock())

        # Assertions can be made here based on the expected behavior of the main function
        # For example, check if the user was prompted again after entering an invalid choice


if __name__ == "__main__":
    unittest.main()

