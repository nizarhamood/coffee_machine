# Below is my test data in dict format
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Coffee function to calulate resources and cost based on selection 
def coffee_output(coffee_type):
    # Returns the amount needed to create the specific coffee type (water/coffee etc)
    coffee_type_water = menu[coffee_type]["ingredients"]["water"]
    coffee_type_coffee = menu[coffee_type]["ingredients"]["coffee"]
    
    #Returns the cost of the selected coffee
    coffee_cost = menu[coffee_type]["cost"]
    print(f"The {coffee_type} costs ${coffee_cost}")
    
    print("Please insert coins.")

    # Calculates the number of coins selected to pay for the coffee
    quarters = int(input("How many quarters? "))
    total_quarters = quarters*0.25
    
    dimes = int(input("How many dimes? "))
    total_dimes = dimes*0.1
    
    nickles = int(input("How many nickles? "))
    total_nickles = nickles*0.05
    
    pennies = int(input("How many pennies? "))
    total_pennies = pennies*0.01

    total = total_quarters + total_dimes + total_nickles + total_pennies

    # If esspresso is selected the below logic is applied
    if coffee_type == "espresso":
        #If resources are greater than amount needed to develop coffee then coffee is produced
        if resources["water"] >= coffee_type_water and resources["coffee"] >= coffee_type_coffee:
            resources["water"] = resources["water"] - coffee_type_water
            resources["coffee"] = resources["coffee"] - coffee_type_coffee
            
            # If total cash selected/inserted is equal to the cost, the coffee is ready
            if total == coffee_cost: 
                print(f"Your {coffee_type} is ready.")
                #print(resources)
            # If the total selected/inserted is greater than the cost, the coffee is ready and change is calculated and returned
            elif total > coffee_cost:
                change = total - coffee_cost

                print(f"Your {coffee_type} is ready. Please collect your drink and {change} change")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"NOT ENOUGH INGREDIENTS TO PRODUCE YOUR ESPRESSO, , please collect your money {total}")
    
    # If latte or cappuccino is seleted, the below logic is applied
    if coffee_type == "latte" or coffee_type == "cappuccino":
        coffee_type_milk = menu[coffee_type]["ingredients"]["milk"]
        #If resources are greater than amount needed to develop coffee then coffee is produced
        if resources["water"] >= coffee_type_water and resources["coffee"] >= coffee_type_coffee and resources["milk"] >= coffee_type_milk:
            resources["water"] = resources["water"] - coffee_type_water
            resources["coffee"] = resources["coffee"] - coffee_type_coffee
            resources["milk"] = resources["milk"] - coffee_type_milk

            # If total cash selected/inserted is equal to the cost the coffee is ready
            if total == coffee_cost:
                print(f"Your {coffee_type} is ready.")
                print(resources)
            # If the total selected/inserted is greater than tcost, the coffe is ready and change is calculated areturned
            elif total > coffee_cost:
                change = total - coffee_cost

                print(f"Your {coffee_type} is ready. Please collect your drink and {change} change")
                #print(resources)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"NOT ENOUGH INGREDIENTS TO PRODUCE YOUR {coffee_type}, please collect your money {total}.")

machine = "on"
while machine == "on":
    coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
    
    # To turn off the coffee machine and exit the while loop
    if coffee == "off":
        machine = "off"
    
    # To check the resources left to make coffee
    elif coffee == "report":
        print(resources)
    
    # If a coffee selection is selected, the below logic runs the coffee function
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        coffee_output(coffee)
