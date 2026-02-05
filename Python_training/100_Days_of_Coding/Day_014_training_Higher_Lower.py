# Higher Lower Game - Instagram Edition
# Data source: Compiled from publicly available information including 
# Wikipedia's "List of most-followed Instagram accounts" and other public sources.
# Dataset compiled by GitHub Copilot (AI Assistant).
# Follower counts are approximate and subject to change.

import json
import random
import os

def load_instagram_data():
    """Load Instagram follower data from JSON file"""
    json_path = os.path.join(os.path.dirname(__file__), 'json_files', 'instagram_data.json')
    with open(json_path, 'r') as file:
        return json.load(file)

def format_account(account):
    """Format account data for display"""
    return f"{account['name']}, a {account['occupation']}, from {account['country']}"

def display_logo():
    """Display game logo"""
    logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
    """
    print(logo)

def display_vs():
    """Display VS symbol"""
    vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
    """
    print(vs)

def play_game():
    """Main game logic"""
    data = load_instagram_data()
    score = 0
    game_continue = True
    
    # Pick first random account
    account_b = random.choice(data)
    
    while game_continue:
        # Account A becomes previous B
        account_a = account_b
        # Pick new account B (make sure it's different)
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
        
        # Display
        print(f"\nCompare A: {format_account(account_a)}")
        display_vs()
        print(f"Against B: {format_account(account_b)}")
        
        # Get user guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess not in ['A', 'B']:
            print("Invalid input. Please type 'A' or 'B'.")
            continue
        
        # Check answer
        followers_a = account_a['followers']
        followers_b = account_b['followers']
        
        is_correct = False
        if followers_a > followers_b and guess == 'A':
            is_correct = True
        elif followers_b > followers_a and guess == 'B':
            is_correct = True
        elif followers_a == followers_b:
            is_correct = True  # Give benefit of doubt for ties
        
        # Clear screen (optional - works in terminal)
        os.system('cls' if os.name == 'nt' else 'clear')
        display_logo()
        
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
            print(f"{account_a['name']} has {followers_a:,} followers.")
            print(f"{account_b['name']} has {followers_b:,} followers.")

def main():
    """Main function to run the game"""
    display_logo()
    print("Welcome to the Higher Lower Game!")
    print("Guess which account has more Instagram followers.\n")
    
    play_again = True
    while play_again:
        play_game()
        response = input("\nPlay again? Type 'yes' or 'no': ").lower()
        if response != 'yes':
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()
