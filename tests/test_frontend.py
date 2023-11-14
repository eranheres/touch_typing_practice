import pytest
from unittest import mock
from touch_typing_practice.frontend import Frontend

class TestFrontend:
    @mock.patch('curses.window.getstr', return_value=b'username')
    def test_get_username(self, mock_getstr):
        frontend = Frontend()
        username = frontend.get_username(mock.MagicMock())
        assert username == 'username'

    @mock.patch('curses.window.getstr', return_value=b'1')
    def test_get_menu_choice(self, mock_getstr):
        frontend = Frontend()
        choice = frontend.get_menu_choice(mock.MagicMock())
        assert choice == 1

    @mock.patch('curses.window.getstr', return_value=b'session text')
    def test_get_session_text(self, mock_getstr):
        frontend = Frontend()
        text = frontend.get_session_text(mock.MagicMock())
        assert text == 'session text'

    @mock.patch('curses.window.getstr', return_value=b'typed text')
    def test_get_typed_text(self, mock_getstr):
        frontend = Frontend()
        typed_text = frontend.get_typed_text(mock.MagicMock())
        assert typed_text == 'typed text'

    @mock.patch('curses.window.addstr')
    def test_display_statistics(self, mock_addstr):
        frontend = Frontend()
        frontend.typing_practice = mock.MagicMock()
        frontend.typing_practice.get_user_statistics.return_value = {'session_time': {'stat': 'value'}}
        frontend.display_statistics(mock.MagicMock())
        mock_addstr.assert_any_call('Session at session_time:\n')
        mock_addstr.assert_any_call('  stat: value\n')

    @mock.patch('curses.window.getstr', side_effect=[b'username', b'1', b'session text', b'typed text', b'3'])
    @mock.patch('curses.window.addstr')
    def test_run(self, mock_addstr, mock_getstr):
        frontend = Frontend()
        frontend.run(mock.MagicMock())
        mock_addstr.assert_any_call('Session ended. Your progress has been recorded.')
