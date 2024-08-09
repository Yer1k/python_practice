"""Module to test the function the_meaning_of_life() in the file the_meaning_of_life.py."""

from unittest.mock import patch
from the_meaning_of_life import the_meaning_of_life  # type: ignore


def test_the_meaning_of_life() -> None:
    """
    Test that the function the_meaning_of_life() prints the correct summary.
    """
    with patch("builtins.input", side_effect=["Alice", "Happiness"]), patch(
        "builtins.print"
    ) as mocked_print:
        the_meaning_of_life()

        # Combine the print outputs into a single string
        expected_output = (
            "\nSUMMARY OF RESULTS\n"
            "\nName ==> Alice\n"
            "\nMeaning of Life ==> Happiness\n"
        )

        # Flatten the actual print calls into a single string
        actual_output = "".join(call[0][0] for call in mocked_print.call_args_list)

        assert actual_output == expected_output
