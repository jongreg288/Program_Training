print("""88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  8b,dPPYba,   
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  88P'   `"8a  
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88  
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  88       88  
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  88       88
                                    aa,    ,88                                
                                     "Y8bbdP"                                            """)

import random
import json

chosen_word = "null"
user_choice = 0

def len_choice():
	global user_choice
	print("Welcome to Hangman!\n")
	user_choice = input("Please choose a number between 5 and 10 for your word length:\n")
	while not user_choice.isdigit() or int(user_choice) < 5 or int(user_choice) > 10:
		user_choice = input("Invalid input. Please choose a number between 5 and 10:\n")
	user_choice = int(user_choice)
	word_list()

def word_list():
	global chosen_word, user_choice
	data = json.load(open("Python_training/100_Days_of_Coding/json_files/words_dictionary.json"))
	words = [word for word in data.keys() if len(word) == user_choice]
	chosen_word = random.choice(words)
#	print(chosen_word)
	hangman()

def hangman():
	global chosen_word, user_choice
	word_length = len(chosen_word)
	lives = user_choice - 1
	print(f"The chosen word has {word_length} letters and you have {lives} lives.")
	display = ['_'] * word_length
	print(' '.join(display))
	guessed_letters = []

	while lives != 0 and '_' in display:
		guess = input("Please guess a letter:\n").lower()
		if len(guess) != 1 or not guess.isalpha():
			print("Invalid input. Please enter a single letter. You still have your lives left.")
			continue
		if guess in guessed_letters:
			print(f"You've already guessed the letter '{guess}'. Try again.")
			continue
		guessed_letters.append(guess)
		if guess in chosen_word:
			for position in range(word_length):
				if chosen_word[position] == guess:
					display[position] = guess
			print(' '.join(display))
		else:
			lives -= 1
			print(f"Wrong guess. You have {lives} lives left.")
			if lives == 0:
				end_of_game = True
				print(f"You lose! The word was '{chosen_word}'.")
		if '_' not in display:
			end_of_game = True
			print("Congratulations! You've guessed the word correctly.")
	if end_of_game:
		restart = input("Would you like to play again? 'yes' or 'no':\n").lower()
		if restart == "yes":
			len_choice()
		else:
			print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
	len_choice()

#credit to dwyl on github for the word dictionary json file
