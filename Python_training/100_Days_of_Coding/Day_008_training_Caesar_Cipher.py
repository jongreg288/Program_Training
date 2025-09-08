print("Welcome to the Caesar Cipher!\n")

direction = ""
text = ""
shift = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def user_prompt():
	global direction, text, shift
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	while direction not in ['encode', 'decode']:
		direction = input("Invalid input. Please type 'encode' or 'decode':\n")

	text = input("Type your message:\n").lower()

	shift = input("Type the shift number:\n")
	while not shift.isdigit():
		shift = input("Invalid input. Please type a whole number:\n")

	shift = int(shift) % 26
	if shift == 0:
		shift = 26

def caesar(start_text, shift_amount, cipher_direction):
	global alphabet
	end_text = ""
	if cipher_direction == "decode":
		shift_amount *= -1
	for char in start_text:
		if char in alphabet:
			position = alphabet.index(char)
			new_position = (position + shift_amount) % 26
			end_text += alphabet[new_position]
		else:
			end_text += char
	print(f"The {cipher_direction}d text is: '{end_text}'\n")

def restart():
	again = input("\nDo you have more to encode or decode? 'Y' or 'N': ").lower()
	if again == 'y':
		main()
	else:
		print("Goodbye!")

def main():
	user_prompt()
	caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
	restart()

if __name__ == "__main__":
	main()
