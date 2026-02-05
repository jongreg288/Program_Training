import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

attempt_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if attempt_level not in ['easy', 'hard']:
	print("Invalid choice. Defaulting to 'hard' mode.")
	attempt_level = 'hard'

if attempt_level == 'easy':
	attempts = 10
else:
	attempts = 5

def number_guessing_game():
	target_number = random.randint(1, 100)
	attempts_remaining = attempts
	while attempts_remaining > 0:
		print(f"You have {attempts_remaining} attempts remaining to guess the number.")
		try:
			guess = int(input("Make a guess: "))
		except ValueError:
			print("Please enter a valid integer.")
			continue

		if guess < 1 or guess > 100:
			print("Your guess is out of bounds. Please guess a number between 1 and 100.")
			continue

		if guess < target_number:
			print("Too low.")
		elif guess > target_number:
			print("Too high.")
		else:
			print(f"Congratulations! You've guessed the number {target_number} correctly!")
			return

		attempts_remaining -= 1

	print(f"Sorry, you've run out of attempts. The number was {target_number}.")
 
number_guessing_game()