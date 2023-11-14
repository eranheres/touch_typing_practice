import unittest
from unittest.mock import Mock
from touch_typing_practice.typing_practice import TypingPractice
from touch_typing_practice.user import User
from touch_typing_practice.session import Session

class TestTypingPractice(unittest.TestCase):
    ## Test Initialization
    def test_init(self):
        user = User("test_user")
        tp = TypingPractice(user)
        self.assertEqual(tp.user, user)
        self.assertIsNone(tp.current_session)

    ## Test Start Session
    def test_start_session(self):
        user = User("test_user")
        tp = TypingPractice(user)
        tp.start_session("test_text")
        self.assertIsInstance(tp.current_session, Session)

    ## Test Start Session Exception
    def test_start_session_exception(self):
        user = User("test_user")
        tp = TypingPractice(user)
        tp.start_session("test_text")
        with self.assertRaises(Exception):
            tp.start_session("test_text")

    ## Test End Session
    def test_end_session(self):
        user = User("test_user")
        tp = TypingPractice(user)
        tp.start_session("test_text")
        tp.end_session("typed_text")
        self.assertIsNone(tp.current_session)

    ## Test End Session Exception
    def test_end_session_exception(self):
        user = User("test_user")
        tp = TypingPractice(user)
        with self.assertRaises(Exception):
            tp.end_session("typed_text")

    ## Test Get User Statistics
    def test_get_user_statistics(self):
        user = User("test_user")
        tp = TypingPractice(user)
        user.get_statistics = Mock(return_value="statistics")
        self.assertEqual(tp.get_user_statistics(), "statistics")

