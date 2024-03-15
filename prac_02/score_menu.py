"""
CP1404 - Practical 2 - Score Menu
Student Name - Khant Zay Yar
Student ID   - 14052564
"""

MENU = """(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    print(MENU)
    score = None
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is None:
                print("Please enter the score first, Press 'G'.")
            else:
                print(determine_score_status(score))
        elif choice == "S":
            if score is None:
                print("Please enter the score first, Press 'G'.")
            else:
                print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score!")
        score = int(input("Enter score: "))
    return score


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print(int(score) * "*")


main()