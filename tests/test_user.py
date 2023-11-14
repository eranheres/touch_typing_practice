import unittest
import os
from touch_typing_practice.user import User
from touch_typing_practice.session import Session

class TestUser(unittest.TestCase):
    def test_init(self):
        user = User('test_user')
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.history, {})

    def test_record_session(self):
        user = User('test_user')
        session = Session('test text')
        session.start()
        session.end('test typed text')
        user.record_session(session)
        self.assertIn(session.start_time.strftime("%Y-%m-%d %H:%M:%S"), user.history)

    def test_get_statistics(self):
        user = User('test_user')
        session = Session('test text')
        session.start()
        session.end('test typed text')
        user.record_session(session)
        self.assertEqual(user.get_statistics(), user.history)

    def test_save(self):
        user = User('test_user')
        session = Session('test text')
        session.start()
        session.end('test typed text')
        user.record_session(session)
        user.save()
        self.assertTrue(os.path.isfile('test_user.json'))

    def test_load(self):
        user = User('test_user')
        session = Session('test text')
        session.start()
        session.end('test typed text')
        user.record_session(session)
        user.save()
        loaded_user = User.load('test_user')
        self.assertEqual(loaded_user.history, user.history)

if __name__ == '__main__':
    unittest.main()
