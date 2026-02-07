import time
from menu import Menu
from make_coffee import MakeCoffee
from coins import Coins


class CoffeeMachine:
    """Main controller class for the coffee machine."""
    
    def __init__(self):
        self.menu = Menu()
        self.maker = MakeCoffee()
        self.payment = Coins()
        self.is_on = True
    
    def display_welcome(self):
        """Displays welcome message."""
        print("\n" + "="*50)
        print("Welcome to the Coffee Machine!")
        print("This machine accepts quarters, dimes, and nickels only.")
        print("(No pennies or bills)")
        print("="*50)
    
    def display_main_menu(self):
        """Displays the main menu options."""
        self.menu.display_menu()
        choice = input("\nWhat would you like? We serve Espresso, Latte, or Cappuccino: ").lower()
        return choice
    
    def process_order(self, choice):
        """Processes the customer's drink order."""
        drink = self.menu.get_drink(choice)
        
        if not drink:
            print("Invalid selection. Please choose again.")
            return
        
        # Check resources
        if not self.maker.is_resource_sufficient(drink.ingredients):
            print("Cannot process order due to insufficient resources.")
            time.sleep(2)
            return
        
        # Process payment
        paid = self.payment.process_coins(drink.cost)
        is_valid, change = self.payment.validate_payment(paid, drink.cost)
        
        if not is_valid:
            time.sleep(2)
            return
        
        # Make the drink
        self.maker.make_drink(drink)
        self.payment.add_earnings(drink.cost)
        time.sleep(2)
    
    def admin_menu(self):
        """Displays the admin menu and processes admin commands."""
        while True:
            print("\n" + "-"*50)
            print("ADMIN MENU")
            print("-"*50)
            print("1. View Resources Report")
            print("2. Refill Resources")
            print("3. View Earnings")
            print("4. Take Earnings")
            print("5. Power Off Machine")
            print("6. Exit Admin Menu")
            
            choice = input("\nEnter your choice (1-6): ").lower()
            
            if choice == "1":
                print(self.maker.get_report())
                print(f"Earnings: ${self.payment.get_earnings():.2f}")
            
            elif choice == "2":
                self.refill_menu()
            
            elif choice == "3":
                print(f"\nCurrent Earnings: ${self.payment.get_earnings():.2f}")
            
            elif choice == "4":
                money_taken = self.payment.take_earnings()
                print(f"\nYou have taken ${money_taken:.2f} from the machine.")
            
            elif choice == "5":
                print("\nShutting down the machine...")
                time.sleep(2)
                self.power_off()
                return
            
            elif choice == "6":
                print("Exiting admin menu.\n")
                return
            
            else:
                print("Invalid selection. Please try again.")
            
            time.sleep(1)
    
    def refill_menu(self):
        """Allows admin to refill resources."""
        print("\n" + "-"*50)
        print("REFILL RESOURCES")
        print("-"*50)
        print("Current levels:")
        print(self.maker.get_report())
        
        while True:
            resource = input("Enter resource to refill (water/milk/coffee) or 'done' to exit: ").lower()
            
            if resource == "done":
                break
            
            if resource not in ["water", "milk", "coffee"]:
                print("Unknown resource. Please try again.")
                continue
            
            try:
                amount = int(input(f"How much {resource} to add? "))
                self.maker.refill_resources(resource, amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def power_off(self):
        """Powers off the machine and offers to turn it back on."""
        self.is_on = False
        print("\nCoffee machine is powered off.")
        
        while True:
            response = input("Would you like to turn it back on? (y/n): ").lower()
            
            if response == "y":
                print("Powering on the coffee machine...")
                time.sleep(2)
                self.is_on = True
                break
            elif response == "n":
                print("Machine remains off. Goodbye!")
                time.sleep(2)
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    
    def run(self):
        """Main loop to run the coffee machine."""
        self.display_welcome()
        
        while self.is_on:
            choice = self.display_main_menu()
            
            if choice == "admin":
                self.admin_menu()
            elif choice == "off":
                self.power_off()
                if not self.is_on:
                    break
            elif self.menu.is_valid_choice(choice):
                self.process_order(choice)
            else:
                print("Invalid selection. Please choose again.")
                time.sleep(1)
        
        print("\nThank you for using the Coffee Machine!")
