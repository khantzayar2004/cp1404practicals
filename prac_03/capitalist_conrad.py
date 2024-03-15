"""
CP1404 - Practical 3 - Capitalist Conrad
Student Name - Khant Zay Yar
Student ID   - 14052564
"""

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 0.01
MAX_PRICE = 100.0
INITIAL_PRICE = 1.0
FILENAME = "stock.txt"

price = INITIAL_PRICE
day = 0
print(f"Starting price: ${price:,.2f}")

out_file = open(FILENAME, 'w')
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1
    # This generates a random integer of 1 or 2
    # If it is 1, the price increases.
    if random.randint(1, 2) == 1:
        # This generates a random floating point number
        # Between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # This generates a random floating point number
        # Between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

out_file.close()