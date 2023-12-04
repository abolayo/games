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
# TODO 1. Output a report
money = 0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
cost_latte = MENU['latte']['cost']
cost_espresso = MENU['espresso']['cost']
cost_cappuccino = MENU['cappuccino']['cost']


def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")





    # TODO 3. Process Coins
def process_coins(quarter, dime, nickle, penny, choose):
    global money
    global milk
    global coffee
    global water

    # TODO 2. Check resource sufficient?
    if (water < 0) or (milk < 0) or (coffee < 0):
        print("insufficient ingredients")
        report()
        exit()
    if choose == 'latte':
        cost = cost_latte
    elif choose == 'espresso':
        cost = cost_espresso
    else:
        cost = cost_cappuccino
    total_paid = ((quarter * 25) + (dime * 10) + (nickle * 5) + penny) / 100
    # TODO 4. Check transcation successfully
    if total_paid < cost:
        print("Sorry that is not enough money, Money refunded.")
    else:
        change = total_paid - cost
        money += cost
        water -= MENU[choose]['ingredients']['water']
        milk -= MENU[choose]['ingredients']['milk']
        coffee -= MENU[choose]['ingredients']['coffee']
        print(f"There is ${change} in change. ")
        print(f"Here is your {choose} enjoy it.")


make_coffee = True
# TODO 5. Make coffee
while make_coffee:
    choose = input('what would you like? (espresso/latte/cappuccino): ').lower()
    if choose == "report":
        report()
        order = input('Would you still like to order. Type "y for yes: ').lower()
        if order != 'y':
            make_coffee = False
    choose = input('what would you like? (espresso/latte/cappuccino): ').lower()
    print('Please insert the coins.')
    quarter = int(input('How many quarters?: '))
    dime = int(input('How many dimes?: '))
    nickle = int(input('How many nickles?: '))
    penny = int(input('How many pennies?: '))
    process_coins(quarter, dime, nickle, penny, choose)

    more = input('Would you still like to order more coffee . Type "y for yes: ').lower()
    if more != 'y':
        print("Thank you for the purchase! Bye")
        make_coffee = False


