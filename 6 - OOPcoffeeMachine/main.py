from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system

_=system("cls")

myMenu=Menu()
myCoffeeMaker=CoffeeMaker()
myMoneyMachine=MoneyMachine()

def machine():
    while True:
        order=input(f"What would you like? ({myMenu.get_items()}): ").lower()
        if order == "off":
            return
        elif order == "report":
            myCoffeeMaker.report()
            myMoneyMachine.report()
        else:
            if not myCoffeeMaker.is_resource_sufficient(myMenu.find_drink(order)):
                continue
            else:
                if myMoneyMachine.make_payment(myMenu.find_drink(order).cost):
                    myCoffeeMaker.make_coffee(myMenu.find_drink(order))

machine()
                
