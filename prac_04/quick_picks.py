"""
CP1404 - Prac 04
"""

import random

NUMBERS_PER_LINE = 6
MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1


def main():
    """Get quick picks."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid")
        number_of_quick_picks = int(input("How many quick picks? "))
    generate_quick_pick(number_of_quick_picks)


def generate_quick_pick(number_of_quick_picks):
    """Generate random quick picks."""
    for row in range(number_of_quick_picks):
        quick_picks = []
        for column in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))


main()