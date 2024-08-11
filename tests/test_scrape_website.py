"""Module to test the scrape_website module."""

from unittest.mock import patch
from scrape_website import scrape_website  # type: ignore


def test_scrape_website() -> None:
    """
    Test that the function scrape_website() prints the correct summary.
    """
    with patch("builtins.print") as mocked_print:
        scrape_website("https://www.yer1k.com/")

        # Combine the print outputs into a single string
        expected_output_list = [
            "https://about.yer1k.com//",
            "https://yer1k.com/blog/",
            "https://yer1k.weebly.com/",
            "https://yer1k.com",
            "https://yer1k.com/project/",
            "https://running.yer1k.com/",
            "https://yer1k.com/",
            "https://www.strava.com/athletes/yer1k",
            "https://github.com/Yer1k",
            "https://www.linkedin.com/in/dyang7/",
            "https://github.com/gersonbdev/ataraxia-zola",
            "https://about.yer1k.com/",
            "https://www.getzola.org/",
            "https://creativecommons.org/licenses/by/4.0/",
            "https://www.instagram.com/yer1k/",
        ]

        actual_output_list = [call[0][0] for call in mocked_print.call_args_list]

        # assert all the links are in the expected output
        for link in expected_output_list:
            assert link in actual_output_list
