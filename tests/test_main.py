import pytest
from unittest.mock import Mock, call
from touch_typing_practice import main

def test_main():
    stdscr = Mock()
    User = Mock()
    TypingPractice = Mock()
    main(stdscr, User, TypingPractice)

    User.load.assert_called_once()
    TypingPractice.assert_called_once_with(User.load.return_value)

def test_main_input_1():
    stdscr = Mock()
    User = Mock()
    TypingPractice = Mock()
    stdscr.getstr.side_effect = ['1', 'test text', 'typed text']
    main(stdscr, User, TypingPractice)

    TypingPractice.return_value.start_session.assert_called_once_with('test text')
    TypingPractice.return_value.end_session.assert_called_once_with('typed text')

def test_main_input_2():
    stdscr = Mock()
    User = Mock()
    TypingPractice = Mock()
    stdscr.getstr.return_value = '2'
    main(stdscr, User, TypingPractice)

    TypingPractice.return_value.get_user_statistics.assert_called_once()

def test_main_input_3():
    stdscr = Mock()
    User = Mock()
    TypingPractice = Mock()
    stdscr.getstr.return_value = '3'
    main(stdscr, User, TypingPractice)

    assert not User.load.called
    assert not TypingPractice.called

def test_main_invalid_choice():
    stdscr = Mock()
    User = Mock()
    TypingPractice = Mock()
    stdscr.getstr.return_value = 'invalid'
    main(stdscr, User, TypingPractice)

    assert not User.load.called
    assert not TypingPractice.called
