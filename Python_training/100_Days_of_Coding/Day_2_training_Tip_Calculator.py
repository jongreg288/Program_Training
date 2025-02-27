import math

print("Welcome to the Tip Calculator")
while True:
	try:
		total_bill = float(input("What was the total bill? \n$ "))
		if total_bill > 0:
			break
		else:
			print("The total bill must be greater than $0.\n") # Negative input handleing
	except ValueError:
		print("Invalid input. Please enter a valid number for the total bill.\n") # Non-numeric input handling
verify = '' # Variable called prior to input to prevent error
while True:
	try:
		tip_percentage = float(input("What percentage tip would you like to give? \n"))
		if tip_percentage >= 0 and tip_percentage <= 100:
			break
		elif tip_percentage > 100 and verify != 'yes': # If the tip percentage is greater than 100, the user is asked to verify
			while True:
				try:
					verify = input("The tip percentage is more than 100, are you sure you wish to tip this amount?\n").lower()
					if verify == 'yes':
						break
					elif verify != 'no' and verify != 'yes':
						print("Invalid input. Please enter yes or no.\n") # Invalid input handling
					elif verify == 'no':
						tip_percentage = float(input("What percentage tip would you like to give? \n")) # If the user does not wish to tip more than 100%, they are asked to re-enter the tip percentage
				except ValueError:
					print("Invalid input. Please enter a valid number for the tip percentage.\n") # Non-numeric input handling
			break
		else:
			print("Invalid input. Please enter a valid number for the tip percentage\n") # Negative input handling
	except ValueError:
		print("Invalid input. Please enter a valid number for the tip percentage.\n") # Non-numeric input handling
while True:
	try:
		people = int(input("How many people to split the bill?\n"))
		if people >= 1:
			break
		else:
			print("The number of people must be a whole number and greater than 0.\n") # Negative and <1 input handling
	except ValueError:
		print("Invalid input. Please enter a valid number for the number of people.\n") # Non-numeric input handling
split_bill = round((total_bill + (total_bill * tip_percentage / 100)) / people, 2)
print(f"Each person should pay: ${split_bill}")
