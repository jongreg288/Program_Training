import math

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

def calculator():
	operations = {
		'+' : add,
		'-' : subtract,
		'*' : multiply,
		'/' : divide
	}
	
	# Get first number
	while True:
		try:
			n1 = float(input("Enter the first number: "))
			break
		except ValueError:
			print("Please enter a valid number.")
	
	should_continue = True
	while should_continue:
		# Get second number
		while True:
			try:
				n2 = float(input("Enter the second number: "))
				break
			except ValueError:
				print("Please enter a valid number.")
		
		# Get operation
		while True:
			operation = input("Choose an operation (+, -, *, /): ")
			if operation in operations:
				break
			else:
				print("Invalid operation. Please choose from +, -, *, /.")

		# Calculate and display result
		result = operations[operation](n1, n2)
		print(f"The result of {n1} {operation} {n2} is: {result}")

		# Ask if user wants to continue with result
		if input("Would you like to perform another calculation with the result? (yes/no): ").lower() == 'yes':
			n1 = result
		else:
			should_continue = False
			if input("Would you like to start a new calculation? (yes/no): ").lower() == 'yes':
				calculator()
			else:
				print("Thank you for using the calculator. Goodbye!")

print("Welcome to the simple calculator!")
calculator()
