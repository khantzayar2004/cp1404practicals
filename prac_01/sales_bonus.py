"""
CP1404 - Practical 1 - Sales Bonus
Student Name - Khant Zay Yar
Student ID   - 14052564
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Bonus is $", bonus, sep='')
    sales = float(input("Enter sales: $"))