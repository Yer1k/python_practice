"""Module to extract countries from a file and print them out."""


def get_contents_of_file(continent_name: str) -> str | None:
    """
    Read the contents of a file for a given continent name.
    """
    try:
        with open(f"../data/{continent_name}.csv", encoding="utf-8") as continent_file:
            lines = continent_file.read()

    except FileNotFoundError:
        lines = None

    return lines


def get_country_dict(country_list: str) -> dict[str, str]:
    """
    Take a list of countries and cities and turn them into a dictionary.
    """
    lines = country_list.splitlines()
    countries = {}

    for line in lines:
        combine = line.split(",")
        country, city = combine
        countries[country] = city

    return countries


def print_results(continent_name: str, countries: dict[str, str]) -> None:
    """
    Print out the countries and cities for a given continent.
    """
    print(continent_name)
    print("-" * len(continent_name))

    for country_name, city_name in countries.items():
        print(f"{country_name} ({city_name})")


if __name__ == "__main__":
    CONTINENT_NAME_DEFAULT = "Oceania"
    country_list_default = get_contents_of_file(CONTINENT_NAME_DEFAULT)

    if country_list_default is None:
        print(f"There are no countries for {CONTINENT_NAME_DEFAULT}")
    else:
        countries_default = get_country_dict(country_list_default)
        print_results(CONTINENT_NAME_DEFAULT, countries_default)
