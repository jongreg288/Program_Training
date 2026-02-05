import time

water_level = 1000  # in ml
milk_level = 500  # in ml
coffee_ground_level = 200  # in g
earnings = 0.00  # in $

def admin_menu():
    # Displays the admin menu options.
    admin_choice = 0
    while admin_choice != 4 and admin_choice != 5:
        admin_choice = int(input("Admin Menu: Report(1), Refill(2), Take Earnings(3), Power off(4), Exit Admin(5): "))
        if admin_choice == 1:
            report()
        elif admin_choice == 2:
            refill_resources()
        elif admin_choice == 3:
            money_taken = take_earnings()
            print(f"You have taken ${money_taken:.2f} from the machine.")
        elif admin_choice == 4:
            print("Powering off the coffee machine.")
            time.sleep(5)  # 5 second pause
            off_mode()
        elif admin_choice == 5:
            print("Exiting admin menu.")
            coffee_machine()
        else:
            print("Invalid selection. Please choose again.")

def report():
    # Prints the current resource levels and money earned.
    print(f"Water: {water_level}ml")
    print(f"Milk: {milk_level}ml")
    print(f"Coffee Grounds: {coffee_ground_level}g")
    print(f"Money Earned: ${earnings:.2f}")
    
def refill_resources():
    # Refills the resources based on user input.
    global water_level, milk_level, coffee_ground_level
    while input("Refill resources? Press Enter to continue, type 'n' to skip, type 'exit' at any prompt to stop: ").lower() not in ['n', 'exit']:
        water = input("Add water? (y/n): ").lower()
        if water == 'n':
            return
        elif water == 'y':
            add_water = int(input(f"How much water to add (in ml)? Maximun of {1000 - water_level}: "))
            water_level += add_water
        elif water == 'exit':
            return
        milk = input("Add milk? (y/n): ").lower()
        if milk == 'n':
            return
        elif milk == 'y':
            add_milk = int(input(f"How much milk to add (in ml)? Maximun of {500 - milk_level}: "))
            milk_level += add_milk
        elif milk == 'exit':
            return
        coffee = input("Add coffee grounds? (y/n): ").lower()
        if coffee == 'n':
            return
        elif coffee == 'y':
            add_coffee = int(input(f"How much coffee grounds to add (in g)? Maximun of {200 - coffee_ground_level}: "))
            coffee_ground_level += add_coffee
        elif coffee == 'exit':
            return
        print("Resources refilled.")
    if input == 'n' or input == 'exit':
        print("Exiting refill menu.")
        return
    
def take_earnings():
    # Empties the earnings and returns the amount taken.
    global earnings
    money_taken = earnings
    earnings = 0.00
    return money_taken

def is_resource_sufficient(drink_ingredients):
    # Returns True if there are sufficient resources to make the drink.
    for item in drink_ingredients:
        if drink_ingredients[item] > globals()[f"{item}_level"]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins(cost):
    # Returns the total calculated from coins inserted.
    print(f"Please insert coins, the total is ${cost:.2f}.")
    paid = int(input("How many quarters?: ")) * 0.25
    paid += int(input("How many dimes?: ")) * 0.10
    paid += int(input("How many nickels?: ")) * 0.05
    return paid

def make_coffee(drink_name, drink_ingredients, cost):
    # Deducts the required ingredients from the resources and adds the cost to earnings.
    global water_level, milk_level, coffee_ground_level, earnings
    for item in drink_ingredients:
        globals()[f"{item}_level"] -= drink_ingredients[item]
    earnings += cost
    print(f"Here is your {drink_name}. Enjoy!")
    time.sleep(2) # brief pause before next prompt
    coffee_machine()

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee_ground": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee_ground": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee_ground": 24,
        },
        "cost": 3.00,
    }
    }

CHOICE_LIST = ["espresso", "latte", "cappuccino", "admin", "off"]

def coffee_machine():
    print("Welcome, this machine does not accept pennies or bills.")
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "admin":
        admin_menu()
    elif choice in MENU:
        drink = MENU.get(choice)
        if drink:
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins(drink["cost"])
                if payment >= drink["cost"]:
                    change = payment - drink["cost"]
                    if change > 0:
                        print(f"Here is ${change:.2f} in change.")
                    make_coffee(choice, drink["ingredients"], drink["cost"])
                else:
                    print("Sorry, that's not enough money. Money refunded.")
                    time.sleep(2) # brief pause before next prompt
                    coffee_machine()
            else:
                print("Cannot process order due to insufficient resources.")
                time.sleep(2) # brief pause before next prompt
                coffee_machine()
        else:
            print("Invalid selection. Please choose again.")
            coffee_machine()
    elif choice == "off":
        print("Powering off.")
        time.sleep(5) # 5 second pause to simulate shutdown
        off_mode()
    else:
        print("Invalid selection. Please choose again.")
        coffee_machine() # In case of invalid input, restart the coffee machine prompt
            
def off_mode():
    input_value = input("Coffee machine is powered off.\n Would you like to turn it back on? (y/n): ").lower()
    if input_value == 'y':
        print("Powering on the coffee machine.")
        time.sleep(2)  # 2 second pause
        coffee_machine()
    elif input_value == 'n':
        time.sleep(5)  # 5 second pause
        off_mode()

if __name__ == "__main__":
    coffee_machine()