"""Module to add two numbers that input from the user, and print the sum of them."""

import sys


def add_two_numbers() -> None:
    """
    Function to add two numbers that input from the user,
    and print the sum of them.
    """
    try:
        number1 = int(input("Enter the first number you want to add:\n"))
        number2 = int(input("Enter the second number you want to add:\n"))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        sys.exit(1)
    nums_sum = number1 + number2
    print(f"The sum of {number1} and {number2} is {nums_sum}.")


if __name__ == "__main__":
    add_two_numbers()
