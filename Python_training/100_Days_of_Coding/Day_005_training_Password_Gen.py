import random

# Create a list of letters, numbers and symbols
list_sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
list_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_let_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_let_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create a list of all the characters
list_all = list_sym + list_num + list_let_upper + list_let_lower

def password_gen():
	global x
	choice = input('Do you want to create a password with user input or randomly? (user/random): ').lower()
	if choice == 'user':
		x = int(input('How many characters do you want your password to be, up to 16 characters: '))
		while x > 16 or x < 1:
			print('Invalid input. Please try again.')
			x = int(input('How many characters do you want your password to be, up to 16 characters: '))
		user_password()
	elif choice == 'random':
		random_password()
	else:
		while choice != 'user' and choice != 'random':
			print('Invalid input. Please try again.')
			choice = input('Do you want to create a password with user input or randomly? (user/random): ').lower()

# Create a password with user input
def user_password():
	global x
	password = []
	for i in range(0, x):
		password.append(random.choice(list_all))
	print(''.join(password))
	acpt = input("Is this password acceptable? y or n: ")
	if acpt == 'n':
		password_gen()
	elif acpt == 'y':
		print('Password accepted. Thank you.')
	else:
		while acpt != 'y' and acpt != 'n':
			print('Invalid input. Please try again.')
			acpt = input("Is this password acceptable? y or n: ")

# Create a password randomly
def random_password():
	password = []
	for i in range(0, 12):
		password.append(random.choice(list_all))
	print(''.join(password))
	acpt = input("Is this password acceptable? y or n: ")
	if acpt == 'n':
		password_gen()
	elif acpt == 'y':
		print('Password accepted. Thank you.')
	else:
		while acpt != 'y' and acpt != 'n':
			print('Invalid input. Please try again.')
			acpt = input("Is this password acceptable? y or n: ")

while __name__ == '__main__':
	password_gen()
	break
