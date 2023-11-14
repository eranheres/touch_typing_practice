import unittest
from unittest.mock import patch, Mock
from touch_typing_practice.main import main

class TestMain(unittest.TestCase):

    @patch('touch_typing_practice.main.User.load')
    def test_valid_username(self, mock_load):
        mock_load.return_value = Mock()
        main(Mock())
        mock_load.assert_called_once()

    @patch('touch_typing_practice.main.TypingPractice.start_session')
    @patch('touch_typing_practice.main.TypingPractice.end_session')
    def test_start_new_session(self, mock_end_session, mock_start_session):
        main(Mock())
        mock_start_session.assert_called_once()
        mock_end_session.assert_called_once()

    @patch('touch_typing_practice.main.TypingPractice.get_user_statistics')
    def test_view_statistics(self, mock_get_user_statistics):
        mock_get_user_statistics.return_value = {}
        main(Mock())
        mock_get_user_statistics.assert_called_once()

    def test_exit_application(self):
        with self.assertRaises(SystemExit):
            main(Mock())

    def test_invalid_choice(self):
        with self.assertRaises(ValueError):
            main(Mock())

    @patch('touch_typing_practice.main.User.load')
    def test_invalid_username(self, mock_load):
        mock_load.side_effect = Exception()
        with self.assertRaises(Exception):
            main(Mock())
        mock_load.assert_called_once()

if __name__ == '__main__':
    unittest.main()
