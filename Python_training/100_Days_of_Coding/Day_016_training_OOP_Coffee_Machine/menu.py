class Drink:
    """Represents a drink item on the coffee machine menu."""
    
    def __init__(self, name, ingredients, cost):
        self.name = name
        self.ingredients = ingredients  # Dictionary of ingredient: amount
        self.cost = cost
    
    def __str__(self):
        return f"{self.name} - ${self.cost:.2f}"


class Menu:
    """Manages the menu of available drinks."""
    
    def __init__(self):
        self.drinks = {
            "espresso": Drink(
                "Espresso",
                {"water": 50, "coffee": 18},
                1.50
            ),
            "latte": Drink(
                "Latte",
                {"water": 200, "milk": 150, "coffee": 24},
                2.50
            ),
            "cappuccino": Drink(
                "Cappuccino",
                {"water": 250, "milk": 100, "coffee": 24},
                3.00
            )
        }
        self.menu_options = ["espresso", "latte", "cappuccino", "admin", "off"]
    
    def get_drink(self, drink_name):
        """Returns a Drink object if it exists, otherwise None."""
        return self.drinks.get(drink_name.lower())
    
    def display_menu(self):
        """Displays available drinks."""
        print("\n--- Available Drinks ---")
        for name, drink in self.drinks.items():
            print(f"{drink}")
    
    def is_valid_choice(self, choice):
        """Checks if the choice is a valid menu option."""
        return choice.lower() in self.menu_options
        