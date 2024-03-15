"""
CP1404 - Prac 04
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display it."""
    subjects = get_subjects()
    display_subjects(subjects)


def get_subjects():
    """Read data from file formatted like code, number of students, lecturer"""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # To see what a line looks like
        print(repr(line))  # To see what a line really looks like
        line = line.strip()  # To remove the \n
        parts = line.split(',')  # To separate the data into its parts
        print(parts)  # To see what the parts look like
        parts[2] = int(parts[2])  # To make the number into integer
        print(parts)  # To see if it worked
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    """Display data neatly."""
    for subject in subjects:
        # Print using the format method
        print("{} is taught by {:12} and has {:3} students".format(*subject))


main()