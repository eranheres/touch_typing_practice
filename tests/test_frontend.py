import pytest
import curses
from touch_typing_practice.frontend import Frontend

class TestFrontend:

    def test_get_user_input(self, monkeypatch):
        monkeypatch.setattr('curses.getstr', lambda x, y, z: b'test')
        frontend = Frontend('test_user')
        assert frontend.get_user_input('Enter text for the session: ', 100) == 'test'

    def test_display_options(self, capsys):
        frontend = Frontend('test_user')
        frontend.display_options()
        captured = capsys.readouterr()
        assert captured.out == "1. Start new session\n2. View statistics\n3. Exit\n"

    def test_start_typing_session(self, monkeypatch):
        monkeypatch.setattr('curses.getstr', lambda x, y, z: b'test')
        frontend = Frontend('test_user')
        frontend.start_typing_session()
        assert frontend.typing_practice.current_session.text == 'test'

    def test_end_typing_session(self, monkeypatch):
        monkeypatch.setattr('curses.getstr', lambda x, y, z: b'test')
        frontend = Frontend('test_user')
        frontend.start_typing_session()
        frontend.end_typing_session()
        assert frontend.typing_practice.current_session is None

    def test_display_user_statistics(self, capsys, monkeypatch):
        monkeypatch.setattr('curses.getstr', lambda x, y, z: b'test')
        frontend = Frontend('test_user')
        frontend.start_typing_session()
        frontend.end_typing_session()
        frontend.display_user_statistics()
        captured = capsys.readouterr()
        assert 'Session at' in captured.out
