"""Module to ask user for their name and what they think is the meaning of life."""


def the_meaning_of_life() -> None:
    """
    Ask user for their name and what they think is the meaning of life,
    then print a summary of the results.
    """
    try:
        person_name = input("What is your name?\n")
        life_meaning = input(
            f"Hello {person_name}, what do you think is the meaning of life?\n"
        )
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except EOFError:
        print("\nProgram interrupted by user.")

    summary = "\nSUMMARY OF RESULTS\n"
    summary += f"\nName ==> {person_name}\n"
    summary += f"\nMeaning of Life ==> {life_meaning}\n"

    print(summary)


if __name__ == "__main__":
    the_meaning_of_life()
