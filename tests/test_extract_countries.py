"""Module to test the extract_countries module."""

from unittest.mock import mock_open, patch
from extract_countries import get_contents_of_file, get_country_dict, print_results  # type: ignore


def test_get_contents_of_file() -> None:
    """Test the get_contents_of_file function."""
    continent_name = "Asia"
    moke_file_data = "China,Beijing\nJapan,Tokyo\nIndia,New Delhi"

    with patch("builtins.open", mock_open(read_data=moke_file_data)) as mock_file:
        countries = get_contents_of_file(continent_name)

    assert moke_file_data in countries

    mock_file.assert_called_once_with("../data/Asia.csv", encoding="utf-8")


def test_get_country_dict() -> None:
    """Test the get_country_dict function."""
    country_list = "China,Beijing\nJapan,Tokyo\nIndia,New Delhi"
    countries = get_country_dict(country_list)

    assert countries == {"China": "Beijing", "Japan": "Tokyo", "India": "New Delhi"}


def test_print_results(capsys: "pytest.CaptureFixture") -> None:  # type: ignore
    """Test the print_results function."""
    continent_name = "Asia"
    countries = {"China": "Beijing", "Japan": "Tokyo", "India": "New Delhi"}

    print_results(continent_name, countries)

    captured = capsys.readouterr()
    assert "Asia\n----\n" in captured.out
    assert "China (Beijing)\n" in captured.out
    assert "Japan (Tokyo)\n" in captured.out
    assert "India (New Delhi)\n" in captured.out
