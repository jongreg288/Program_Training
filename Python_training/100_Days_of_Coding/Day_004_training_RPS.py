import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice; rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Try again, choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!", 1, 0
    else:
        return "You lose!", 0, 1

def play_game():
    user_wins = 0
    computer_wins = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result, user_win, computer_win = determine_winner(user_choice, computer_choice)
        user_wins += user_win
        computer_wins += computer_win
        print(result)
        print(f"Score - You: {user_wins}, Computer: {computer_wins}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Final Score - You: {user_wins}, Computer: {computer_wins}")
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    play_game()
