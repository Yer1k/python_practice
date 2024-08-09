"""Module to test the add_two_numbers function from slack_add.py."""

from unittest.mock import patch
from slack_add import add_two_numbers  # type: ignore


def test_add_two_numbers() -> None:
    """
    Test that the function add_two_numbers() prints the correct sum.
    """
    with patch("builtins.input", side_effect=[2, 3]), patch(
        "builtins.print"
    ) as mocked_print:
        add_two_numbers()

        expected_output = "The sum of 2 and 3 is 5."
        actual_output = mocked_print.call_args_list[0][0][0]

        assert actual_output == expected_output
