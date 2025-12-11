import random

print("Welcome to The Blackjack Game!")

balance = 1000

face_cards = {
'J' : 10,
'Q' : 10,
'K' : 10
}

def deal_card():
	"""Returns a random card from the deck."""
	cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
	return random.choice(cards)

def calculate_score(cards):
	"""Calculate the score of the given cards."""
	score = 0
	for card in cards:
		if card in face_cards:
			score += face_cards[card]
		elif card == 'A':
			if score + 11 > 21:
				score += 1
			else:
				score += 11
		else:
			score += card
	return score

def place_bets():
	"""Player places their bet."""
	print(f"Your current balance: {balance}")
	bet = input("Enter your bet amount: ")
	while not bet.isdigit() or int(bet) <= 0:
		bet = input("Invalid bet amount. Please enter a positive integer: ")
	if int(bet) > balance:
		bet = input(f"Insufficient balance. Please enter a valid bet amount (max {balance}): ")
		while not bet.isdigit() or int(bet) <= 0 or int(bet) > balance:
			bet = input(f"Invalid bet amount. Please enter a valid bet amount (max {balance}): ")
	return int(bet)

def play_game():
	global balance
	"""Play a round of the Blackjack game."""
	bet = place_bets()
	player_cards = [deal_card(), deal_card()]
	dealer_cards = [deal_card(), deal_card()]
	while True:
		player_score = calculate_score(player_cards)
		dealer_score = calculate_score(dealer_cards)
		if player_score == 21 and dealer_score != 21:
			break
		elif player_score > 21:
			break
		else:
			print(f"Your cards: {player_cards}, current score: {player_score}")
			print(f"Dealer's first card: {dealer_cards[0]}")
			another_card = input("Type 'y' to hit, type 'n' to pass: ")
			while another_card.lower() != 'y' and another_card.lower() != 'n':
				another_card = input("Invalid input. Type 'y' to hit, type 'n' to pass: ")
			if another_card.lower() == 'y':
				player_cards.append(deal_card())
			else:
				break
	
	# Check if cards have same value (10, J, Q, K all equal 10)
	card1_value = face_cards.get(player_cards[0], player_cards[0])
	card2_value = face_cards.get(player_cards[1], player_cards[1])
	
	if card1_value == card2_value:
		split_choice = input("You have a matched pair, would you like to split? (y/n): ").lower()
		if split_choice == 'y':
			# Split the hand and play two separate hands
			player_cards_1 = [deal_card(), deal_card()]
			player_cards_2 = [deal_card(), deal_card()]
			player_cards_1[0] = player_cards[0]
			player_cards_2[0] = player_cards[1]
			dealer_cards = [deal_card(), deal_card()]
			while calculate_score(dealer_cards) < 17:
				dealer_cards.append(deal_card())
			print(f"Your first hand: {player_cards_1}, final score: {calculate_score(player_cards_1)}")
			print(f"Your second hand: {player_cards_2}, final score: {calculate_score(player_cards_2)}")
			print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
			if calculate_score(player_cards_1) > 21 and calculate_score(player_cards_2) > 21:
				print("Both hands bust! You lose.")
				balance -= bet * 2
			elif calculate_score(player_cards_1) > 21:
				print("Your first hand busts! You lose on that hand.")
				balance -= bet
			elif calculate_score(player_cards_2) > 21:
				print("Your second hand busts! You lose on that hand.")
				balance -= bet
			else:
				if calculate_score(player_cards_1) > calculate_score(dealer_cards):
					print("You win on the first hand!")
					balance += bet
				elif calculate_score(player_cards_1) < calculate_score(dealer_cards):
					print("You lose on the first hand.")
					balance -= bet
				else:
					print("It's a tie on the first hand, bet refunded.")

				if calculate_score(player_cards_2) > calculate_score(dealer_cards):
					print("You win on the second hand!")
					balance += bet
				elif calculate_score(player_cards_2) < calculate_score(dealer_cards):
					print("You lose on the second hand.")
					balance -= bet
				else:
					print("It's a tie on the second hand, bet refunded.")
		else:
			while calculate_score(dealer_cards) < 17:
				dealer_cards.append(deal_card())
			print(f"Your final hand: {player_cards}, final score: {calculate_score(player_cards)}")
			print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")

			if calculate_score(player_cards) > 21:
				print("You bust! You lose.")
				balance -= bet
			elif calculate_score(dealer_cards) > 21:
				print("Dealer busts! You win!")
				balance += bet
			elif calculate_score(player_cards) > calculate_score(dealer_cards):
				print("You win!")
				balance += bet
			elif calculate_score(player_cards) < calculate_score(dealer_cards):
				print("You lose.")
				balance -= bet
			else:
				print("It's a tie, bet refunded.")
	else:
		# Normal game ending (no matching pair)
		while calculate_score(dealer_cards) < 17:
			dealer_cards.append(deal_card())
		print(f"Your final hand: {player_cards}, final score: {calculate_score(player_cards)}")
		print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
		
		if calculate_score(player_cards) > 21:
			print("You bust! You lose.")
			balance -= bet
		elif calculate_score(dealer_cards) > 21:
			print("Dealer busts! You win!")
			balance += bet
		elif calculate_score(player_cards) > calculate_score(dealer_cards):
			print("You win!")
			balance += bet
		elif calculate_score(player_cards) < calculate_score(dealer_cards):
			print("You lose.")
			balance -= bet
		else:
			print("It's a tie, bet refunded.")

	another_game = input(f"Your new balance is {balance}.\nDo you want to play another game? (y/n): ")
	while another_game.lower() != 'y' and another_game.lower() != 'n':
		another_game = input("Invalid input. Do you want to play another game? (y/n): ")
	if another_game.lower() == 'y':
		play_game()
	else:
		print("Thank you for playing!")

if __name__ == "__main__":
	play_game()