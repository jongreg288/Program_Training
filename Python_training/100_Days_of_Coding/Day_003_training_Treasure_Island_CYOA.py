print(r"""  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/""")

ded = 0
win = 0

def treasure_island():
	global ded, win
	print("Welcome to Treasure Island.")
	print("Your mission is to find the treasure.")
	fork()

def fork():
	direction_01 = input("You come to a fork in the road. Do you go 'left' or 'right'?\n").lower()
	while direction_01 != "left" and direction_01 != "right":
		direction_01 = input("You may want to follow the road here.\nChoose 'left' or 'right':\n").lower()
	if direction_01 == "left":
		lake()
	elif direction_01 == "right":
		woods()

def lake():
	global ded, win
	lake = input("You come to a lake, there's an island in the middle of it. Do you 'swim' or 'wait' for a boat?\n").lower()
	while lake != "swim" and lake != "wait":
		lake = input("You take a nice nap by the lake, but decide it's time to carry on.\nChoose 'swim' or 'wait':\n").lower()
	if lake == "wait":
		house_01 = input("A boat arrives and takes you to the island. You see three small houses. Which one do you enter? 'left', 'middle', or 'right'?\n").lower()
		while house_01 != "left" and house_01 != "middle" and house_01 != "right":
			house_01 = input("You decide to explore the island.\nIt's a rather small island and you soon come back to the houses.\nChoose 'left', 'middle', or 'right':\n").lower()
		if house_01 == "left":
			print("You enter the house on the left and are greeted by the love of your life.\nYou live happily ever after.\nFor love is the greatest treasure there is.")
			win += 1
			print(f"Wins: {win}, Deaths: {ded}")
			again = input("Would you like to play again? 'yes' or 'no':\n").lower()
			if again == "yes":
				treasure_island()
			else:
				print("Thank you for playing!")
		elif house_01 == "right":
			print("You enter the house on the right and are greeted by a witch.\nShe turns you into a frog.")
			ded += 1
			print(f"Wins: {win}, Deaths: {ded}")
			again = input("Would you like to play again? 'yes' or 'no':\n").lower()
			if again == "yes":
				treasure_island()
			else:
				print("Thank you for playing!")
		elif house_01 == "middle":
			middle_house = input("You enter the house in the middle, it seems to be empty.\nDo you want to explore the house? 'yes' or 'no'\n").lower()
			while middle_house != "yes" and middle_house != "no":
				print("This does seem like a good place to stay a while, and listen.")
				middle_house = input("Do you want to explore the house? 'yes' or 'no'\n").lower()
			if middle_house == "yes":
				print("You find a hidden door leading to the basement.\nThere's treasure stashed in the basement!\nYou live richly every after.")
				win += 1
				print(f"Wins: {win}, Deaths: {ded}")
				again = input("Would you like to play again? 'yes' or 'no':\n").lower()
				if again == "yes":
					treasure_island()
				else:
					print("Thank you for playing!")
			else:
				print("You decide to leave the house and are bitten by a snake.\nYou die.")
				ded += 1
				print(f"Wins: {win}, Deaths: {ded}")
				again = input("Would you like to play again? 'yes' or 'no':\n").lower()
				if again == "yes":
					treasure_island()
				else:
					print("Thank you for playing!")
	else:
		print("You try to swim to the island and are eaten by a shark.\nThere are always sharks in these waters.")
		ded += 1
		print(f"Wins: {win}, Deaths: {ded}")
		again = input("Would you like to play again? 'yes' or 'no':\n").lower()
		if again == "yes":
			treasure_island()
		else:
			print("Thank you for playing!")

def woods():
	global ded, win
	woods_01 = input("The road takes you through a forest, but you soon lose trake of it.\nDo you search 'left' or 'right' for the road?\n").lower()
	while woods_01 != "left" and woods_01 != "right":
		woods_01 = input("You may want to find the road before it gets dark.\nChoose 'left' or 'right':\n").lower()
	if woods_01 == "left":
		print("You stumble upon a swarm of wasps and are stung to death.")
		ded += 1
		print(f"Wins: {win}, Deaths: {ded}")
		again = input("Would you like to play again? 'yes' or 'no':\n").lower()
		if again == "yes":
			treasure_island()
		else:
			print("Thank you for playing!")
	elif woods_01 == "right":
		meadow_01 = input("You exit the woods into a meadow, would you like to go 'left', 'right', or 'straight'?\n").lower()
		while meadow_01 != "left" and meadow_01 != "right" and meadow_01 != "straight":
			meadow_01 = input("You may want to find safety before it gets dark.\nFor the night is dark and full of terror.\nChoose 'left', 'right', or 'straight':\n").lower()
		if meadow_01 == "left":
			print("You're surrounded by a pack of hungry wolves.\nYou've met with a terrible fate, haven't you?")
			ded += 1
			print(f"Wins: {win}, Deaths: {ded}")
			again = input("Would you like to play again? 'yes' or 'no':\n").lower()
			if again == "yes":
				treasure_island()
			else:
				print("Thank you for playing!")
		elif meadow_01 == "right":
			river()
		elif meadow_01 == "straight":
			hole = input("You find a hole in the ground, do you 'jump' in or 'walk' around it?\n").lower()
			while hole != "jump" and hole != "walk":
				hole = input("This doesn't seem like a good time to dilly-dally.\nChoose 'jump' or 'walk':\n").lower()
			if hole == "jump":
				print("You jump into the hole and are impaled on a stalagmite.\nYou die a slow and painful death.")
				ded += 1
				print(f"Wins: {win}, Deaths: {ded}")
				again = input("Would you like to play again? 'yes' or 'no':\n").lower()
				if again == "yes":
					treasure_island()
				else:
					print("Thank you for playing!")

def river():
	global ded, win
	river = input("You come to a river, do you 'follow' it or go for a 'swim'?\n").lower()
	while river != "follow" and river != "swim":
		river = input("This doesn't seem like a good time to dilly-dally.\nChoose 'follow' or 'swim':\n").lower()
	if river == "follow":
		lake()
	else:
		print("You try to swim across the river and are swept away by the current.\nYou drown.")
		ded += 1
		print(f"Wins: {win}, Deaths: {ded}")
		again = input("Would you like to play again? 'yes' or 'no':\n").lower()
		if again == "yes":
			treasure_island()
		else:
			print("Thank you for playing!")

if __name__ == "__main__":
	treasure_island()
