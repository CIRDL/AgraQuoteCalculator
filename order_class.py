from calculations import *


class Order:

    def __init__(self, square_footage_price, diameter_tank, depth_tank):
        self.square_footage_price = square_footage_price
        self.diameter_tank = diameter_tank
        self.diameter_liner = self.diameter_tank + 1
        self.depth_tank = depth_tank
        self.total_liners = 1

    def __get_floor_square_footage(self):
        floor_square_footage = self.diameter_liner ** 2
        return round(floor_square_footage)

    def __get_wall_square_footage(self):
        side_wall_square_footage = Order.get_liner_circumference(self) * self.depth_tank
        return round(side_wall_square_footage)

    # Legit square footage without 5% or foot added
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
        square_footage = Order.get_actual_square_footage(self, "total") + five_percent
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
        circumference_tank = self.diameter_liner * math.pi
        return circumference_tank

    def get_liner_cost(self):
        liner_cost = Order.get_square_footage(self) * self.square_footage_price
        return liner_cost

    def get_total_liners_cost(self, liner_numbers):
        total_liners_cost = Order.get_liner_cost(self) * liner_numbers
        return total_liners_cost

    def set_total_liners(self, num_liners_added):
        self.total_liners += num_liners_added
        return self.total_liners

    def get_single_layer_geo_cost(self, section):
        geo_wall_cost = round(Order.get_actual_square_footage(self, "wall") * 0.4, 2)
        geo_floor_cost = round(Order.get_actual_square_footage(self, "floor") * 0.4, 2)
        if section[0].lower() == "w":
            return geo_wall_cost
        elif section[0].lower() == "f":
            return geo_floor_cost
        else:
            return geo_wall_cost + geo_floor_cost

    # Don't know if multiple layers will be necessary yet
    def get_total_geo_cost(self):
        raise NotImplementedError

    def get_jbolt_cost(self):
        jbolt_cost = 20
        jbolt_num = math.ceil(Order.get_tank_circumference(self) / 1.5)
        total_jbolt_cost = jbolt_cost * jbolt_num
        return total_jbolt_cost

    # Too tired, not wise to do right now
    def get_installation_cost(self):
        raise NotImplementedError
