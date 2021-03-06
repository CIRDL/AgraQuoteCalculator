from calculations import *
import math


class Order:

    def __init__(self, square_footage_price, diameter_tank, depth_tank):
        self.square_footage_price = square_footage_price
        self.diameter_tank = diameter_tank
        self.diameter_liner = self.diameter_tank + 1
        self.depth_tank = depth_tank
        self.depth_liner = depth_tank + 1
        self.total_liners = 1
        self.discounted = False
        self.discounted_single_liner_cost = 0
        # Order.get_square_footage(self) * self.square_footage_price
        self.lifting_hem_cost = 0

    def get_single_lining_system(self):
        single_lining_sys = Order.get_single_liner_cost(self) + Order.get_batten_strip_cost(self) \
                            + Order.get_lifting_hem_cost(self) + Order.get_jbolt_cost(self) \
                            + Order.get_single_layer_geo_cost(self, "both")
        return single_lining_sys

    def get_total_lining_system(self):
        return Order.get_single_lining_system(self) * self.total_liners

    def __get_floor_square_footage(self):
        floor_square_footage = self.diameter_liner ** 2
        return round(floor_square_footage)

    def __get_wall_square_footage(self):
        side_wall_square_footage = Order.get_liner_circumference(self) * self.depth_liner
        return round(side_wall_square_footage)

    def get_actual_square_footage(self, section):
        if section[0].lower() == "f":
            return Order.__get_floor_square_footage(self)
        elif section[0].lower() == 'w':
            return Order.__get_wall_square_footage(self)
        else:
            return Order.__get_floor_square_footage(self) + Order.__get_wall_square_footage(self)

    # Square footage used to charge stuff
    def get_square_footage(self):
        five_percent = Order.get_actual_square_footage(self, "total") * 0.05
        if self.lifting_hem_cost > 0:
            five_percent = (Order.get_actual_square_footage(self, "total") + Order.get_liner_circumference(self)) * 0.05
        square_footage = math.ceil(Order.get_actual_square_footage(self, "total") + five_percent)
        return round(square_footage)

    # Check legit calculations before charging stuff
    def print_square_footage(self):
        print("Side wall square footage: {:,} ft.".format(Order.get_actual_square_footage(self, "wall")))
        print("Bottom square footage: {:,} ft.".format(Order.get_actual_square_footage(self, "floor")))
        print("Total tank square footage: {:,} ft.".format(Order.get_actual_square_footage(self, "total")))

    def get_tank_circumference(self):
        circumference_tank = self.diameter_tank * math.pi
        return circumference_tank

    def get_liner_circumference(self):
        circumference_liner = self.diameter_liner * math.pi
        return circumference_liner

    def get_single_liner_cost(self):
        liner_cost = Order.get_square_footage(self) * self.square_footage_price
        if self.discounted:
            liner_cost = Order.__get_liner_discount(self)
        return liner_cost

    def get_total_liners_cost(self):
        total_liners_cost = Order.get_single_liner_cost(self) * self.total_liners
        return total_liners_cost

    def get_total_liners(self):
        return self.total_liners

    def set_total_liners(self, num_liners_added):
        self.total_liners += num_liners_added

    def get_single_layer_geo_cost(self, section):
        geo_wall_cost = round(Order.get_actual_square_footage(self, "wall") * 0.4, 2)
        geo_floor_cost = round(Order.get_actual_square_footage(self, "floor") * 0.4, 2)
        if section[0].lower() == "w":
            return geo_wall_cost
        elif section[0].lower() == "f":
            return geo_floor_cost
        else:
            return geo_wall_cost + geo_floor_cost

    def get_jbolt_cost(self):
        jbolt_cost = 20
        jbolt_num = Order.get_jbolt_number(self)
        total_jbolt_cost = jbolt_cost * jbolt_num
        return total_jbolt_cost

    def get_jbolt_number(self):
        return math.ceil(Order.get_tank_circumference(self) / 1.5)

    def calc_installation_cost(self):
        if self.diameter_tank <= 50:
            return 14500
        elif self.diameter_tank <= 69:
            return 15500
        elif self.diameter_tank <= 79:
            return 17500
        elif self.diameter_tank <= 99:
            return 20500
        elif self.diameter_tank <= 110:
            return 22500
        else:
            return 0

    def set_liner_discount(self, discounted_amount_percentage):
        if discounted_amount_percentage > 0:
            self.discounted = True
        discounted_amount_number = discounted_amount_percentage / 100
        self.discounted_single_liner_cost = Order.get_single_liner_cost(self) - (Order.get_single_liner_cost(self)
                                          * discounted_amount_number)

    def __get_liner_discount(self):
        return self.discounted_single_liner_cost

    def set_lifting_hem_cost(self):
        self.lifting_hem_cost = Order.get_liner_circumference(self) * self.square_footage_price * 1.5

    def get_lifting_hem_cost(self):
        return self.lifting_hem_cost

    def get_batten_strip_cost(self):
        batten_strip_cost = 42
        total_batten_strip_cost = batten_strip_cost * (Order.get_tank_circumference(self) / 8)
        return total_batten_strip_cost

