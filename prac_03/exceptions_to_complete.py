"""
CP1404 - Practical 3 - Exceptions To Complete
Student Name - Khant Zay Yar
Student ID   - 14052564
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is: ", result)