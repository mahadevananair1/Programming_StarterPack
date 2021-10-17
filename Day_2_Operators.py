#!/bin/python3
import math
#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = (tip_percent/100) * meal_cost
    tax_cost = (tax_percent/100) * meal_cost
    total = tip_cost + tax_cost + meal_cost
    print(round(total))
    return 0;

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
