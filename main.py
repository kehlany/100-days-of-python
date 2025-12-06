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
# TODO 1:create a function to produce either espresso, latte and capuccino
# def coffe_type(type):
#     water = MENU[type]["ingredients"].get("water", 0)
#     milk = MENU[type]["ingredients"].get("milk", 0)
#     coffee = MENU[type]["ingredients"].get("coffee",0)
#     cost = MENU[type]["cost"]
# coffe_type("latte")
#TODO 2:
gameover = True
while gameover:
    check = input("what would you like? espresso, latte, capuccino")
    def availability(type):
        ingredients = MENU[type]["ingredients"]
        for item in ingredients:
           if resources[item] < ingredients[item]:
               print(f"sorry, you do not have enough {item}")
        for item in ingredients:
            resources[item] -= ingredients[item]
            if input == "report":
                print(resources)
        penny = float(input("how many penny"))
        penny = float(0.01 * penny)
        dime = float(input("how many dime?"))
        dime = 0.10 * dime
        nickel = float(input("how many nickel"))
        nickel = 0.05 * nickel
        quarter = float(input("how many quarter?"))
        quarter = 0.25 * quarter
        total = penny + dime + nickel + quarter
        price_cost = MENU[type]["cost"]
        if total > price_cost:
            change = total - price_cost
            change = round(change,2)
            print(f"here is your change: ${change}")
            print(f"here is your {type} coffee ☕")
        elif total < price_cost:
            print(f"your money is insufficient, you've been refunded{total}")
            gameover = False
    availability(check)
