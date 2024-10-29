

MENU = {
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


 # TODO: 1. Print report of all coffee machine resources
def report(rem_resources, money):
    for key in rem_resources:
        print(f"{key}: {rem_resources[key]}ml")
    print(f"Money: ${money}")

def check_resource(order):
    for key in MENU[order]["ingredients"]:
        if key in resources:
            if resources[key] >= MENU[order]["ingredients"][key]:
                return  True
            else:
                print(f"Sorry there is not enough {key}")
                return False





money = 0
turn_on = True
while turn_on:
    preference = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if preference == "report":
        report(resources, money)
    # print(MENU["latte"]["ingredients"])
    elif preference == "off":
        turn_on = False
    else:
        if check_resource(preference):
            for key in resources:
                if key in MENU[preference]["ingredients"]:
                    resources[key] -= MENU[preference]["ingredients"][key]
            cost = MENU[preference]["cost"]
            money += cost
            # report(resources, money)
        # print("Please insert coin")
            quarters = int(input("How many quarters?: ")) * 0.01
            dimes = int(input("How many dimes?:")) * 0.1
            nickles = int(input("How many nickles?:")) * 0.05
            pennies = int(input("How many pennies?:")) * 0.25

            total_money  = quarters + dimes + nickles + pennies

            if total_money >= cost:
                print(f"Here is ${total_money - cost} in change.")
                print(f"Here is your {preference} Enjoy!")

            else:
                print("Insufficient amount")





