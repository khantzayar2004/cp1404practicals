"""
CP1404 - Practical 1 - Loops
Student Name - Khant Zay Yar
Student ID   - 14052564
"""

# odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end='')
print()

# a.
for i in range(0, 101, 10):
    print(i, end='')
print()

# b.
for i in range(20, 0, -1):
    print(i, end='')

# c.
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end='')
print()

# d.
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()