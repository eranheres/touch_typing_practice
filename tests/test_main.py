import unittest
from unittest.mock import Mock, patch
from touch_typing_practice import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.stdscr = Mock()
        self.user = Mock()
        self.typing_practice = Mock()
        self.user_patcher = patch('touch_typing_practice.main.User', return_value=self.user)
        self.typing_practice_patcher = patch('touch_typing_practice.main.TypingPractice', return_value=self.typing_practice)
        self.user_patcher.start()
        self.typing_practice_patcher.start()

    def tearDown(self):
        self.user_patcher.stop()
        self.typing_practice_patcher.stop()

    def test_main_start_new_session(self):
        self.stdscr.getstr.side_effect = ['username', '1', 'text', 'typed_text']
        main(self.stdscr)
        self.typing_practice.start_session.assert_called_once_with('text')
        self.typing_practice.end_session.assert_called_once_with('typed_text')

    def test_main_view_statistics(self):
        self.stdscr.getstr.side_effect = ['username', '2']
        main(self.stdscr)
        self.typing_practice.get_user_statistics.assert_called_once()

    def test_main_exit(self):
        self.stdscr.getstr.side_effect = ['username', '3']
        main(self.stdscr)

    def test_main_invalid_choice(self):
        self.stdscr.getstr.side_effect = ['username', 'invalid', '3']
        main(self.stdscr)

if __name__ == '__main__':
    unittest.main()
