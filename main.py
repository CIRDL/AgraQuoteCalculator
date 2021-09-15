# @author Cesar Ramirez
# @program Agra Quote Calculator

from error import *
from calculations import converter
from calculations import diameter_modifier
from customizations import *
from order_class import Order

# Collect price per square foot
sqft_price = input("Enter price per square foot: $")
empty_response = empty_string(sqft_price)
sqft_price = empty_literal(empty_response, "Please enter price per square foot: $", sqft_price)
sqft_price = float(sqft_price)

# DIAMETER configuration
diameter_ft = input("Enter diameter of tank (ft): ")
empty_response = empty_string(diameter_ft)
diameter_ft = empty_literal(empty_response, "Please enter diameter of tank (ft): ", diameter_ft)
diameter_ft = float(diameter_ft)

diameter_inch = input("Enter any remaining inches: ")
empty_response = empty_string(diameter_inch)
diameter_inch = empty_literal(empty_response, "Please enter any remaining inches: ", diameter_inch)
diameter_inch = float(diameter_inch)
diameter_tank = converter(diameter_ft, diameter_inch)
diameter_liner = diameter_modifier(diameter_tank)

# DEPTH configuration
depth_ft = input("Enter depth of tank (ft): ")
empty_response = empty_string(depth_ft)
depth_ft = empty_literal(empty_response, "Please enter depth of tank (ft): ", depth_ft)
depth_ft = float(depth_ft)

depth_inch = input("Enter any remaining inches: ")
empty_response = empty_string(depth_inch)
depth_inch = empty_literal(empty_response, "Please enter any remaining inches: ", depth_inch)
depth_inch = float(depth_inch)

depth_tank = converter(depth_ft, depth_inch)

print("")

# Create object
quote = Order(sqft_price, diameter_tank, depth_tank)

# Print square footage
Order.print_square_footage(quote)

# Prints out cost of single liner
print("\nQuote cost of liner: ${:,.2f}".format(Order.get_liner_cost(quote)))

# Prompt for customization loop
print("\nCustomize order below:\nType \'help\' for options\nType \'back\' for menu\n------------------------\n")

# Setup for customization loop
order_list = []
satisfied = False
discounted = False
total_quote_cost = Order.get_liner_cost(quote)

# Customization loop
while not satisfied:

    # Reset back button
    back_button = False

    # Get user command
    command = input("> ").lower()

    # To finish the order
    if command == 'finish':
        satisfied = True
        print("\nOrder Completed")
        continue

    # GEO
    elif command[0] == 'g' and command[1] == 'e':

        geo_satisfied = False

        # TODO - SEE IF NECESSARY TO INCLUDE MORE THAN ONE LAYER OPTION
        # LAYERS
        # Sets both default layers to one
        total_geo_wall_layers = 1
        total_geo_floor_layers = 1
        needs_more_geo_layers = input("\nWould you like to add more layers (yes/no)? ").lower()
        # Back button
        if needs_more_geo_layers[0] == 'b' or needs_more_geo_layers[0] == 'B':
            print("")
            continue

        if needs_more_geo_layers[0] == 'y':

            while not geo_satisfied:

                additional_geo_layers = input("Enter number of layers you wish to add: ")
                empty_response = empty_string(additional_geo_layers)
                additional_geo_layers = empty_literal(empty_response, "Please enter number of layers you wish to add: ",
                                                      additional_geo_layers)
                additional_geo_layers = int(additional_geo_layers)

                additional_geo_layer_section = input("Is additional geo padding for 'wall', 'floor', or 'both': ") \
                    .lower()
                if additional_geo_layer_section[0] == 'w':
                    total_geo_wall_layers += additional_geo_layers
                elif additional_geo_layer_section[0] == 'f':
                    total_geo_floor_layers += additional_geo_layers
                else:
                    total_geo_wall_layers += additional_geo_layers
                    total_geo_floor_layers += additional_geo_layers

                is_geo_satisfied = input("Would you like to add more layers (yes/no)? ").lower()
                if is_geo_satisfied[0] == 'n':
                    geo_satisfied = True

        # Finds cost of order's layers of geo
        total_geo_cost = Order.get_single_layer_geo_cost(quote, "wall") * total_geo_wall_layers + \
            Order.get_single_layer_geo_cost(quote, "floor") * total_geo_floor_layers

        total_quote_cost += total_geo_cost

        # Keep track of order
        order_list.append("geo")

        if needs_more_geo_layers[0] == 'y':
            print("\nCost of single layer of geo: ${:,.2f}".format(Order.get_single_layer_geo_cost(quote, "both")))
            print("Cost of total geo added: ${:,.2f}".format(total_geo_cost))
            print("Total quote cost: ${:,.2f}\n".format(total_quote_cost))
        else:
            print("\nCost of single layer of geo added: ${:,.2f}".format(
                Order.get_single_layer_geo_cost(quote, "both")))
            print("Total quote cost: ${:,.2f}\n".format(total_quote_cost))

    # J-BOLTS
    elif command[0] == 'j':
        # Accounts in total quote cost
        total_quote_cost += Order.get_jbolt_cost(quote)

        # Keep track of order
        order_list.append("jbolt")

        print("\nCost of j-bolts added: ${:,.2f}".format(Order.get_jbolt_cost(quote)))
        print("\nTotal quote cost: ${:,.2f}\n".format(total_quote_cost))

    # INSTALLATION
    elif command[0] == 'i' and command[1] == 'n':

        # For back button
        customized_installation_cost = False

        # Calculates cost of installation per diameter length
        if diameter_tank <= 50:
            installation_cost = 14500
        elif diameter_tank <= 69:
            installation_cost = 15500
        elif diameter_tank <= 79:
            installation_cost = 17500
        elif diameter_tank <= 99:
            installation_cost = 20500
        elif diameter_tank <= 110:
            installation_cost = 22500
        else:
            installation_cost = input("\nPlease enter installation cost: $")
            customized_installation_cost = True
            empty_response = empty_string(installation_cost)
            # Back button
            if not empty_response and (installation_cost[0] == 'b' or installation_cost[0] == 'B'):
                print("")
                continue
            else:
                installation_cost = empty_literal(empty_response, "Please enter installation cost: $",
                                                  installation_cost)
                if installation_cost[0] == 'b' or installation_cost[0] == 'B':
                    print("")
                    continue
                installation_cost = float(installation_cost)

        # Figures cost of traveling
        if not customized_installation_cost:
            miles_traveled = input("\nEnter number of miles being charged: ")
            empty_response = empty_string(miles_traveled)
            if not empty_response and (miles_traveled[0] == 'b' or miles_traveled[0] == 'B'):
                print("")
                continue

            else:
                miles_traveled = empty_literal(empty_response, "Please enter number of miles being charged: "
                                               , miles_traveled)
                if miles_traveled[0] == 'b' or miles_traveled[0] == 'B':
                    print("")
                    continue
                miles_traveled = int(miles_traveled)
        if customized_installation_cost:
            miles_traveled = input("Enter number of miles being charged: ")
            empty_response = empty_string(miles_traveled)
            if empty_response:
                miles_traveled = empty_literal(empty_response, "Please enter number of miles being charged: "
                                               , miles_traveled)
                miles_traveled = int(miles_traveled)

        travel_cost = miles_traveled * 450
        print('Standard travel costs ${:,.2f}.'.format(travel_cost))
        modified_travel_cost = input("Would you like to change it (yes/no)? ").lower()
        empty_response = empty_string(modified_travel_cost)
        if empty_response:
            modified_travel_cost = empty_literal(empty_response, "Please enter yes or no: ", modified_travel_cost)
        if modified_travel_cost[0] == 'y':
            travel_cost = input("Enter travel cost: $")
            empty_response = empty_string(travel_cost)
            if empty_response:
                travel_cost = empty_literal(empty_response, "Please enter travel cost: $", travel_cost)
            travel_cost = int(travel_cost)

        # Calculates total cost
        total_installation_cost = installation_cost + travel_cost

        # Accounts costs
        total_quote_cost += total_installation_cost

        # Keep track of order
        order_list.append("installation")

        # Prints out info
        print("\nCost of installation added: ${:,.2f}".format(installation_cost))
        print("Cost of mileage & mobilization added: ${:,.2f}".format(travel_cost))
        print("\nTotal cost of package added: ${:,.2f}\n".format(total_installation_cost))

    # ADD liners
    elif command[0] == 'a' and command[1] == 'd':

        # Collect number of liners
        additional_liners = input("\nEnter number of liners you wish to add: ")
        if additional_liners[0] == 'b' or additional_liners[0] == 'B':
            print("")
            continue
        else:
            additional_liners = int(additional_liners)

        # Calculate total cost of liners
        additional_liners_cost = liner_cost * additional_liners
        if discounted:
            additional_liners_cost = discounted_liner_cost * additional_liners

        # Adds total liners of order
        total_liners += additional_liners
        total_liners_cost += additional_liners_cost

        # Calculate total cost
        total_quote_cost += additional_liners_cost

        # TODO - might have to add the whole lining system once it's in the program

        # Print out final info
        print("\nCost of additional liners added: ${:,.2f}".format(additional_liners_cost))
        print("Total cost of all liners: ${:,.2f}\n".format(total_liners_cost))

    # DISCOUNT liner price
    elif command[0] == 'd' and command[1] == 'i':

        # Collect desired amount of discount
        discount_amount_percentage = input("\nEnter percentage you wish to discount liner price: ")
        if discount_amount_percentage[0] == 'b' or discount_amount_percentage[0] == 'B':
            print("")
            continue
        else:
            discount_amount_percentage = float(discount_amount_percentage)
        discount_amount_number = discount_amount_percentage / 100

        # Calculate discounted liner cost
        amount_discounted = discount_amount_number * liner_cost
        discounted_liner_cost = liner_cost - amount_discounted

        # For final info
        discounted = True

        # Subtract old liner(s) cost
        if total_liners > 1:
            original_liners_cost = total_liners * liner_cost
        else:
            original_liners_cost = liner_cost

        total_quote_cost -= original_liners_cost

        # Add new liner(s) cost
        if total_liners > 1:
            new_liners_cost = total_liners * discounted_liner_cost
        else:
            new_liners_cost = discounted_liner_cost

        total_quote_cost += new_liners_cost

        # Prints out new info
        print("\nCost of new liner with " + str(discount_amount_percentage) +
              "% discount: ${:,.2f}".format(discounted_liner_cost))
        if total_liners > 1:
            print("Total new liners cost: ${:,.2f}\n".format(new_liners_cost))
        else:
            print()

    # Lifting hem
    elif command[0] == 'l' and command[1] == 'i':

        # For quote document
        lifting_hem = True

        # Cost calculation
        lifting_hem_cost = circumference_liner * sqft_price * 1.5

        # Calculate total cost
        total_quote_cost += lifting_hem_cost

        # Keep track of order
        order_list.append("lifting hem")

        # Print out final info
        print("\nCost of lifting hem added: ${:,.2f}\n".format(lifting_hem_cost))

    # Batten strips
    elif command[0] == "b" and command[1] == 'a':

        # Cost per batten strip
        # TODO - FIGURE IT OUT
        batten_strip_cost = 42

        # Total cost
        total_batten_strip_cost = batten_strip_cost * (circumference_tank / 8)

        # Calculate total quote cost


    # Help commands
    elif command == 'help':
        print("\nCustomizations available:"
              "\n--------------------------\nGeo\nJ-bolts\nInstallation\nLifting hem\nBatten strips"
              "\nAdd liner(s)\nDiscount liner\n\nTo complete order enter \'finish\'\n\n")

    # For user mistake
    else:
        print("\nPlease enter help if you need command list\n")
