"""Use BeautifulSoup to compile a list of external links for any website"""

import requests
from bs4 import BeautifulSoup


def scrape_website(target_url: str) -> None:
    """
    Function to scrape a website for external links.
    """
    # get the HTML page for this
    try:
        html_page = requests.get(target_url, timeout=5).text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    # get the HTML soup for this using default parser
    soup = BeautifulSoup(html_page, "html.parser")

    # get all the hyperlinks
    links = soup.find_all("a")  # a: anchor tag for hyperlinks

    # external links
    external_links = []

    # list them out
    for link in links:

        # get this link's URL
        url = str(link.get("href"))

        # if external link, add it to list
        if not url.startswith("/"):
            if url.startswith("http"):
                external_links.append(url)

    # get list of unique links
    unique_links = set(external_links)
    final_list = list(unique_links)

    if not final_list:
        print("No links found")
    else:
        # list final links out
        for final_link in final_list:
            print(f"{final_link}")


if __name__ == "__main__":

    # TARGET_URL_DEFAULT = "https://www.google.com/"
    TARGET_URL_DEFAULT = "https://www.yer1k.com/"

    scrape_website(TARGET_URL_DEFAULT)
