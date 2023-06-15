from data import MENU,resources
from os import system,name

def printReport():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def checkIngredients(flavor):
    ingredients=MENU[flavor]["ingredients"]
    if ingredients["water"]>resources["water"]:
        print("Sorry there is not enough water.")
        return False
    if ingredients["milk"]>resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if ingredients["coffee"]>resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True

def countMoney(quarters, nickels, dimes, pennies):
    total=0.25*quarters + 0.1*nickels + 0.05*dimes + 0.01*pennies
    return total

# def checkCost(flavor, moneyGiven):
#     if MENU[flavor]["cost"]>moneyGiven:
#         return "Sorry that's not enough money. Money refunded."
#     else:
#         change=moneyGiven-MENU[flavor]['cost']
#         return f"Here is ${'%.2f' % change} dollars in change."

def checkCost(flavor, moneyGiven):
    if MENU[flavor]["cost"]>moneyGiven:
        return False
    else:
        change=moneyGiven-MENU[flavor]['cost']
        return change

def remainingIngredients(flavor):
    resources["water"]-=MENU[flavor]["ingredients"]["water"]
    resources["milk"]-=MENU[flavor]["ingredients"]["milk"]
    resources["coffee"]-=MENU[flavor]["ingredients"]["coffee"]

def machine():
    isContinue=""
    while isContinue!="off":
        isContinue=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if isContinue == "report":
            printReport()
            continue
        elif isContinue == "off":
            continue
        else:
            flavor=isContinue
            if not checkIngredients(flavor):
                continue
            quarters=float(input("How many quarters?: "))
            nickels=float(input("How many nickels?: "))
            dimes=float(input("How many dimes?: "))
            pennies=float(input("How many pennies?: "))
            moneyGiven=countMoney(quarters=quarters,nickels=nickels,dimes=dimes,pennies=pennies)
            if isinstance(checkCost(flavor,moneyGiven),bool):
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                change=checkCost(flavor, moneyGiven)
                print(f"Here is ${'%.2f' % change} dollars in change.")
            resources["money"]+=MENU[flavor]["cost"]
            print(f"Here is your {flavor} ☕. Enjoy!")
            remainingIngredients(flavor)

if name == "nt":
    _=system("cls")
else:
    _=system("clear")

machine()




