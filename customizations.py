# @purpose Shortcuts for customizations section
import math


# Calculates cost for single wall layer of geo
def single_wall_geo_cost(wall_sqft):
    cost = round(wall_sqft * 0.4, 2)
    return cost


# Calculates cost for single floor layer of geo
def single_floor_geo_cost(floor_sqft):
    cost = round(floor_sqft * 0.4, 2)
    return cost


#
