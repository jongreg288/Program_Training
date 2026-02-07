class MakeCoffee:
    """Manages the resources and drink preparation."""
    
    def __init__(self):
        self.water = 1000      # in ml
        self.milk = 500        # in ml
        self.coffee = 200  # in g
    
    UNITS = {
        "water": "ml",
        "milk": "ml",
        "coffee": "g"
    }
    
    def is_resource_sufficient(self, ingredients):
        """Checks if there are enough resources to make the drink."""
        for ingredient, amount in ingredients.items():
            if getattr(self, ingredient, 0) < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True
    
    def make_drink(self, drink):
        """Deducts resources and returns a success message."""
        if not self.is_resource_sufficient(drink.ingredients):
            return False
        
        for ingredient, amount in drink.ingredients.items():
            current_level = getattr(self, ingredient)
            setattr(self, ingredient, current_level - amount)
        
        print(f"Here is your {drink.name}. Enjoy!")
        return True
    
    def refill_resources(self, ingredient, amount):
        """Refills a specific resource."""
        max_levels = {
            "water": 1000,
            "milk": 500,
            "coffee": 200
        }
        
        if ingredient not in max_levels:
            print(f"Unknown ingredient: {ingredient}")
            return False
        
        current = getattr(self, ingredient)
        new_level = min(current + amount, max_levels[ingredient])
        setattr(self, ingredient, new_level)
        print(f"{ingredient} refilled to {new_level}{self.UNITS[ingredient]}")
        return True
    
    def get_report(self):
        """Returns a formatted string of current resource levels."""
        report = f"""
--- Resource Report ---
Water: {self.water}{self.UNITS['water']}
Milk: {self.milk}{self.UNITS['milk']}
Coffee Grounds: {self.coffee}{self.UNITS['coffee']}
"""
        return report