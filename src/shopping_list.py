"""Use a list to create a shopping list and change an item in the list."""


def change_shopping_list(index: int, item: str) -> None:
    """
    Demo of how to change an item in a shopping list.
    """
    shopping_list = ["Double cream", "Single cream", "Eggs", "Oreos"]
    shopping_list[index] = item

    summary = "\nSHOPPING LIST\n"
    summary = summary + "\n" + "\n\n".join(shopping_list)
    print(summary)


if __name__ == "__main__":
    change_shopping_list(3, "Healthier option")
