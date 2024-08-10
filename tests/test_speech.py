"""Module for testing the word counts of the length of words in a speech."""

from unittest.mock import patch
from speech import analyse_word_counts  # type: ignore


def test_analyse_word_counts() -> None:
    """
    Test the analyse_word_counts function.
    """
    # Random speech
    speech = (
        "How are you doing today? I hope you are doing well. \n"
        "I am doing well, thank you for asking."
    )

    with patch("builtins.print") as mocked_print:
        analyse_word_counts(speech)

        # Combine the print outputs into a single string
        expected_output = (
            "\nNumber of words = 19"
            "\n1-letter words = 2"
            "2-letter words = 1"
            "3-letter words = 7"
            "4-letter words = 3"
            "5-letter words = 5"
            "6-letter words = 1"
            "\nCheck total: 19"
        )

        actual_output = "".join(call[0][0] for call in mocked_print.call_args_list)

        assert actual_output == expected_output
