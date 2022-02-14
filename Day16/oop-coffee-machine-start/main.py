from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()
machine_status = True
while(machine_status):
    user_input = input("What would you like? (espresso/latte/cappuccino/report): ").lower()
    if user_input == "report":
        machine.report()
        money_machine.report()
        continue
    if user_input == "off":
        machine_status = False
        continue
    user_input = menu.find_drink(user_input)
    if(machine.is_resource_sufficient(user_input)):
        if(money_machine.make_payment(user_input.cost)):
            machine.make_coffee(user_input)
