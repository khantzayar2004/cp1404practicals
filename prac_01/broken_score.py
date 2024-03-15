"""
CP1404 - Practical 1 - Broken Score
Student Name - Khant Zay Yar
Student ID   - 14052564
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")