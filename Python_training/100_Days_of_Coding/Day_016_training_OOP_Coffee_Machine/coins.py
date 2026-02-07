class Coins:
    """Manages payment processing and earnings for the coffee machine."""
    
    CURRENCY = "USD"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
    }
    
    def __init__(self):
        self.earnings = 0.00
    
    def process_coins(self, cost):
        """Collects coins from the user and returns the total paid."""
        print(f"Please insert coins. Total needed: ${cost:.2f}")
        print("This machine accepts quarters, dimes, and nickels only (no pennies or bills).\n")
        
        paid = int(input("How many quarters?: ")) * self.COIN_VALUES["quarters"]
        paid += int(input("How many dimes?: ")) * self.COIN_VALUES["dimes"]
        paid += int(input("How many nickels?: ")) * self.COIN_VALUES["nickels"]
        
        return paid
    
    def validate_payment(self, paid, cost):
        """Checks if payment is sufficient and returns change."""
        if paid >= cost:
            change = paid - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True, change
        else:
            print(f"Sorry, that's not enough money. You need ${cost - paid:.2f} more.")
            print("Money refunded.")
            return False, paid
    
    def add_earnings(self, amount):
        """Adds the given amount to the earnings."""
        self.earnings += amount
    
    def take_earnings(self):
        """Empties the earnings and returns the amount taken."""
        money_taken = self.earnings
        self.earnings = 0.00
        return money_taken
    
    def get_earnings(self):
        """Returns the current earnings."""
        return self.earnings