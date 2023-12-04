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
# TODO 1. Output a report content
money = 0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
choose = input('what would you like? (espresso/latte/cappuccino): ').lower()


# TODO 2. Output report format
def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


# TODO 3. Calculate cost of chosen coffee
def cal_cost(choose):
    cost_coffee = MENU[choose]['cost']
    return cost_coffee


def update_report(choose):
    global water, milk, coffee
    water -= MENU[choose]['ingredients']['water']
    milk -= MENU[choose]['ingredients']['milk']
    coffee -= MENU[choose]['ingredients']['coffee']


# TODO 4. Process Coins
def process_coins(quarter, dime, nickle, penny, choose):
    global money
    global milk
    global coffee
    global water

    # TODO 5. Check resource sufficient?
    if ((water < MENU[choose]['ingredients']['water'])
            or
            (milk < MENU[choose]['ingredients']['milk'])
            or
            (coffee < MENU[choose]['ingredients']['coffee'])):
        print("insufficient ingredients available")
        report()
        exit()
    cost = cal_cost(choose)
    total_paid = ((quarter * 25) + (dime * 10) + (nickle * 5) + penny) / 100
    # TODO 5. Check transcation successfully
    if total_paid < cost:
        print("Sorry that is not enough money, Money refunded.")
    else:
        change = total_paid - cost
        money += cost
        update_report(choose)
        print(f"There is ${change} in change. ")
        print(f"Here is your {choose} enjoy it.")


# make_coffee = True
# TODO 5. Make coffee
def make_coffee(choose):
    print('Please insert the coins.')
    quarter = int(input('How many quarters?: '))
    dime = int(input('How many dimes?: '))
    nickle = int(input('How many nickles?: '))
    penny = int(input('How many pennies?: '))
    process_coins(quarter, dime, nickle, penny, choose)

    more = input('Would you still like to order more coffee . Type "y for yes: ').lower()
    if more == 'y':
        choose = input('what would you like? (espresso/latte/cappuccino): ').lower()
        make_coffee(choose)
    else:
        print("Thank you for the purchase! Bye")
        exit()


if choose != "report":
    make_coffee(choose)
else:
    report()
    order = input('Would you still like to order. Type "y for yes: ').lower()
    if order == 'y':
        choose = input('what would you like? (espresso/latte/cappuccino): ').lower()
        make_coffee(choose)
    else:
        print("Thank you")
        exit()
