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

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

cash_box = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_ingredients(ingredients):


    for item in ingredients:  # In this part it should be cautious about what loop is going through.
        if resources[item] < ingredients[item]:
            print(f"Sorry not enough {item}")
            return False
    return True


def payment():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * QUARTERS
    total += int(input("how many quarters?: ")) * DIMES
    total += int(input("how many quarters?: ")) * NICKLES
    total += int(input("how many quarters?: ")) * PENNIES
    return total


def is_enough_money(cost, total_money):

    if total_money >= cost:
        change = total_money - cost
        print(f"Here is ${round(change, 2)} in change")
        # you're trying to modify it without declare as global scope
        global cash_box
        cash_box += cost
        return True
    else:
        return False


def make_coffee(req_ingredients):
    for item in req_ingredients:
        resources[item] -= req_ingredients[item]


# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False

    # TODO 3. Print report of all coffee machine resources

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${cash_box}")

    # TODO 4. Check resources sufficient to make drink order.
    # TODO 5. Process coins
    # TODO 6. Check transaction successful?
    # TODO 7. Make Coffee

    elif choice in MENU:
        drink = MENU[choice]
        if check_ingredients(drink["ingredients"]):
            total = payment()
            if is_enough_money(drink["cost"], total):
                make_coffee(drink["ingredients"])
                print(f"Here is your {choice} ☕. Enjoy! ")
            else:
                print("Sorry not enough money. Money Refunded.")

    else:
        print("Invalid Input")
