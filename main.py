# from prettytable import PrettyTable
# table=PrettyTable()
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()

is_on=True

#print report
# coffee_maker.report()
# money_machine.report()

#check if resources sufficient
while is_on:
        options=menu.get_items()
        choice=input(f"What would you like? {options}: ")
        if choice == "off":
            is_on=False
        elif choice=="report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink=menu.find_drink(choice)
            print(drink)
            if coffee_maker.is_resource_sufficient(drink):
        # check if coins sufficient and check if it is successful
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
