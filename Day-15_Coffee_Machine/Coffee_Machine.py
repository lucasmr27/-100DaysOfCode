from menu import MENU


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: R${money}')


def check_resources(request):
    for ingredient in request:
        if request[ingredient] >= resources[ingredient]:
            return False
    print('ok')
    return True


def insert_coin():
    print('Please insert coins.')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    return quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.00

print(MENU['espresso']['ingredients']['water'])


while True:
    flavour = input("What would you like? (espresso/latte/cappuccino):").lower()
    if flavour in [x for x in MENU]:
        check_resources(MENU[flavour]['ingredients'])
        money += insert_coin()
    elif flavour == 'report':
        report()
        continue
    else:
        print("Invalid flavour")
        continue

    break
