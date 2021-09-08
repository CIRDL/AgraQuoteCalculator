# @purpose Shortcuts for calculating general quote
import math


# Converts imperial measurements to double
def converter(feet, inches):
    total_converted = feet + (inches / 12)
    return total_converted


# Adds 1 foot of extra length to diameter (as per requested)
def diameter_modifier(diameter):
    diameter += 1
    return diameter


# Calculates wall square footage of a circular liner
def tank_wall_sq_footage(circumference, depth):

    side_wall = round(circumference * depth)
    print("Side wall square footage: {:,} ft.".format(side_wall))
    return side_wall


# Calculates floor square footage of a circular liner
def tank_floor_sq_footage(diameter):

    floor = round(diameter ** 2)
    print("Bottom square footage: {:,} ft.".format(floor))
    return floor

