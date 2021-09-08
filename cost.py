import math
from calculations import *


class Order:

    def __init__(self, sqft_price, diameter_tank, depth_tank,):
        self.sqft_price = sqft_price
        self.diameter_tank = diameter_tank
        self.depth_tank = depth_tank

    def get_circumference(self):
        circumference_tank = self.diameter_tank * math.pi
        return circumference_tank

    def __get_floor_square_footage(self):
        floor_square_footage = round(self.diameter_tank ** 2)
        return floor_square_footage

    def __get_wall_square_footage(self):
        side_wall_square_footage = round(Order.get_circumference(self) * self.depth_tank)
        return side_wall_square_footage

    def get_square_footage(self, section):
        if section[0].lower() == "f":
            return Order.__get_floor_square_footage(self)
        elif section[0].lower() == 'w':
            return Order.__get_wall_square_footage(self)
        else:
            return Order.__get_floor_square_footage(self) + Order.__get_wall_square_footage(self)

    def print_square_footage(self):
        print("Bottom square footage: {:,} ft.".format(Order.get_square_footage(self, "floor")))
        print("Side wall square footage: {:,} ft.".format(Order.get_square_footage(self, "wall")))
        print("Total tank square footage: {:,} ft.".format(Order.get_square_footage(self, "both")))

