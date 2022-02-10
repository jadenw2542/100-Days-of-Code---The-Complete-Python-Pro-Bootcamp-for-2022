import math
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
    "money": 0.00,
}
def calculate_money(quarters, dimes, nickels, pennies):
    return round((quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01), 2)


def print_resources(resources):
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')


def check_resources(resources, ingredients):
    if resources["water"] < ingredients["water"]:
        print("Sorry there is not enough water")
        return True
    if resources["coffee"] < ingredients["coffee"]:
        print("Sorry there is not enough coffee")
        return True
    if "milk" in ingredients:
        if resources["milk"] < ingredients["milk"]:
            print("Sorry there is not enough milk")
            return True
    return False

def make_drink(resources, ingredients):
    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    if "milk" in ingredients:
        resources["milk"] -= ingredients ["milk"]

    return resources
print("Jaden's coffee vending machine \n"
      "Expresso: $1.50 \n"
      "Latte:  $2.50\n"
      "Cappuccino: $3.00\n")
while(True):
    type_drink = input("What would you like? (espresso/latte/cappuccino/report): ").lower()
    if type_drink == "report":
        print_resources(resources)
        continue
    drink = MENU[type_drink]
    if check_resources(resources, drink["ingredients"]):
        continue
    print("Please insert coins")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    total_money = calculate_money(quarters, dimes, nickels, pennies)
    if total_money < drink["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        continue

    resources = make_drink(resources, drink["ingredients"])
    resources["money"] += drink["cost"]
    total_money -= drink["cost"]
    print(f"Here is ${round(total_money,2)} in change. Enjoy!")




