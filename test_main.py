import unittest
from unittest import mock
from touch_typing_practice import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.stdscr = mock.Mock()
        self.user = mock.Mock()
        self.typing_practice = mock.Mock()
        main.curses = mock.Mock()
        main.User = mock.Mock(return_value=self.user)
        main.TypingPractice = mock.Mock(return_value=self.typing_practice)

    def test_main_start_session(self):
        self.stdscr.getstr.side_effect = [b'username', b'1', b'text', b'typed_text']
        main.main(self.stdscr)
        self.typing_practice.start_session.assert_called_once_with('text')
        self.typing_practice.end_session.assert_called_once_with('typed_text')

    def test_main_view_statistics(self):
        self.stdscr.getstr.side_effect = [b'username', b'2']
        main.main(self.stdscr)
        self.typing_practice.get_user_statistics.assert_called_once()

    def test_main_exit(self):
        self.stdscr.getstr.side_effect = [b'username', b'3']
        with self.assertRaises(SystemExit):
            main.main(self.stdscr)

    def test_main_invalid_choice_non_integer(self):
        self.stdscr.getstr.side_effect = [b'username', b'invalid', b'3']
        with self.assertRaises(SystemExit):
            main.main(self.stdscr)
        self.assertEqual(self.stdscr.getstr.call_count, 3)

    def test_main_invalid_choice_not_option(self):
        self.stdscr.getstr.side_effect = [b'username', b'4', b'3']
        with self.assertRaises(SystemExit):
            main.main(self.stdscr)
        self.assertEqual(self.stdscr.getstr.call_count, 3)

if __name__ == '__main__':
    unittest.main()
