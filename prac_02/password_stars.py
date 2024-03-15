"""
CP1404 - Practical 2 - Password
Student Name - Khant Zay Yar
Student ID   - 14052564
"""


MINIMUM_LENGTH = 10


def version_1():
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
        print('*' * len(password))


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()