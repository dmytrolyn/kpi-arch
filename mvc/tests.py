import unittest
from unittest.mock import patch, call
from io import StringIO
from model import User
from view import View
from controller import Controller


class TestHandler(unittest.TestCase):
    def setUp(self):
        self.user = User("Dmytro")
        self.view = View()
        self.controller = Controller(self.user, self.view)

    def test_handle_user_input(self):
        model = User("Dmytro")
        view = View()
        controller = Controller(model, view)

        input_values = ["display", "update", "Petro", "display", "exit"]
        expected_output = ["Info: Dmytro", "Info: Petro"]

        with patch("builtins.print") as mock_print:
            with patch("builtins.input", side_effect=input_values):
                controller.handle_user_input()

        mock_print.assert_has_calls([call(output) for output in expected_output])

    def test_handle_user_input_custom_input(self):
        model = User("Dmytro")
        view = View()
        controller = Controller(model, view)

        input_values = ["random"]
        expected_output = ["Error: Invalid command."]

        with patch("builtins.print") as mock_print:
            with patch("builtins.input", side_effect=input_values):
                controller.handle_user_input()

        mock_print.assert_has_calls([call(output) for output in expected_output])


if __name__ == "__main__":
    unittest.main()