from unittest.mock import patch
from src.theMeaningofLife import theMeaningOfLife


def test_theMeaningOfLife():
    with patch("builtins.input", side_effect=["Alice", "Happiness"]), patch(
        "builtins.print"
    ) as mocked_print:
        theMeaningOfLife()

        # Combine the print outputs into a single string
        expected_output = (
            "\nSUMMARY OF RESULTS\n"
            "\nName ==> Alice\n"
            "\nMeaning of Life ==> Happiness\n"
        )

        # Flatten the actual print calls into a single string
        actual_output = "".join(call[0][0] for call in mocked_print.call_args_list)

        assert actual_output == expected_output
