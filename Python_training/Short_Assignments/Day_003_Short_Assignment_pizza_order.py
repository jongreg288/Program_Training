print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ").lower()
while size != "s" and size != "m" and size != "l":
	print("Please enter a valid size.") # Invalid input handling
	size = input("What size pizza do you want? S, M, or L ").lower()

add_pepperoni = input("Do you want pepperoni? Y or N ").lower()

while add_pepperoni != "y" and add_pepperoni != "n":
	print("Please enter a valid option.") # Invalid input handling
	add_pepperoni = input("Do you want pepperoni? Y or N ").lower()

extra_cheese = input("Do you want extra cheese? Y or N ").lower()

while extra_cheese != "y" and extra_cheese != "n":
	print("Please enter a valid option.") # Invalid input handling
	extra_cheese = input("Do you want extra cheese? Y or N ").lower()

bill = 0

if size == "s":
	bill += 15
	if add_pepperoni == "y":
		bill += 2
elif size == "m":
	bill += 20
	if add_pepperoni == "y":
		bill += 3
elif size == "l":
	bill += 25
	if add_pepperoni == "y":
		bill += 3
if extra_cheese == "y":
	bill += 1
 
print(f"Your final bill is: ${bill}.")
