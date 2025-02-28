test = ""
exit_command = "exit"

while test.lower() != exit_command:
	test = input("Enter a number (or type 'exit' to quit): ")
	if test.lower() == exit_command:
		break
	if test.isnumeric():
		if int(test) % 2 == 0:
			print("Even")
		else:
			print("Odd")
	else:
		test_count = sum(not c.isdigit() for c in test)
		if test_count % 2 == 0:
			print("Even")
		else:
			print("Odd")
