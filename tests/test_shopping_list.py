"""Module to test the function change_shopping_list() in the file shopping_list.py."""

from unittest.mock import patch
from shopping_list import change_shopping_list  # type: ignore


def test_change_shopping_list() -> None:
    """
    Test that the function change_shopping_list() prints the correct summary.
    """
    with patch("builtins.print") as mocked_print:
        change_shopping_list(3, "Healthier option")

        # Combine the print outputs into a single string
        expected_output = (
            "\nSHOPPING LIST\n"
            "\nDouble cream\n"
            "\nSingle cream\n"
            "\nEggs\n"
            "\nHealthier option"
        )

        # Flatten the actual print calls into a single string
        actual_output = "".join(call[0][0] for call in mocked_print.call_args_list)

        assert actual_output == expected_output
