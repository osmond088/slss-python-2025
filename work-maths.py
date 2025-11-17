# Maths Stuff with Python
# Author: Osmond
# 12 November 2025
#
#

import math

# Do math things with Python
# Machines are good at crunching numbers - faster
# and more accurately than most humans!
# Create a small program that calculates something useful
# to you (making you smile is useful). It should take
# user input, at use at least one of the number
# operators we saw in class: + / * -. You may modify one
# of your previous exercises to include calculations,
# if you wish.


def rectangle_calculator(length: float, width: float) -> tuple:
    """Calculate area and perimeter of a rectangle"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


def main():
    print("Welcome to the Rectangle Calculator!")
    print("This program calculates the area and perimeter of a rectangle.")
    print()

    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    area, perimeter = rectangle_calculator(length, width)

    print(f"\nFor a rectangle with length {length} and width {width}:")
    print(f"  Area = {area:.2f} square units")
    print(f"  Perimeter = {perimeter:.2f} units")


if __name__ == "__main__":
    main()
