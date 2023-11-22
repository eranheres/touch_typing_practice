from unittest.mock import patch

import pytest
from touch_typing_practice.frontend import Frontend


class TestFrontend:
    def setup(self):
        self.frontend = Frontend("test_user")

    def test_start_session(self):
        with patch('builtins.input', return_value="test text"):
            self.frontend.start_session()
        assert self.frontend.typing_practice.current_session is not None

    def test_display_statistics(self):
        with patch('builtins.print') as mock_print:
            self.frontend.display_statistics()
        mock_print.assert_called()

    def test_run(self):
        with patch('builtins.input', side_effect=["1", "test text", "test text", "3"]):
            with patch('builtins.print') as mock_print:
                self.frontend.run()
        mock_print.assert_called_with("Session ended. Your progress has been recorded.")
