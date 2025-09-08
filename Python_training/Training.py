import datetime
import random

print("Hello, World!")

x = 5
y = 3.14 #float
z = 4
a = (x+y+z)

print(x)
print(y)
print(z)
print(a)

print(type(a))

print("Enter your name:")
n1 = input()
print("Hello, " + n1)

print("Hello,  World!"[4]) # prints the character at index 4
print("123" + "345") # concatenates the two numbers
print(123_456_789) # underscores are ignored in numbers, used for readability

n2 = input("Enter your birth year:")
m1 = str((datetime.datetime.now().year)-int(n2))
print("Your age is " + m1)

a = "The quick brown fox jumps over the lazy dog"
print(a.split(" "))
list1 = a.split(" ") # splits the string into a list of words
print(len(list1))
a1 = a.replace(" ", "") # removes spaces from the string
print(a1)
print(len(a1))
list2 = {char: a.count(char) for char in set(a) if char.isalpha()} # counts the frequency of each character in the string
print(list2)
sorted_list2 = dict(sorted(list2.items(), key=lambda item: item[1], reverse=True)) # sorts the dictionary in descending order of frequency
print(sorted_list2)
sorted_list1 = sorted(a1) # sorts the string in alphabetical order
print(sorted_list1)

r1 = 1
list_44 = []
while True: # infinite loop
    x = random.randint(1, 20)
    y = r1
    r1 += 1
    list_44.append(x)
    if x == 13:
        break
    else:
        continue
print("The number 13 has been found")
print("The number of iterations is " + str(y)) # prints the number of iterations
print("The numbers generated are " + str(list_44)) # prints the numbers generated
print("The number of times each number is generated is as follows:") # prints the frequency of each number
for i in set(list_44):
    print(str({i: list_44.count(i)}))

# clear() - removes all elements from the list
# del - removes the item at the specified index
# del list_name - deletes the list
# pop() - removes the last item from the list
# pop(index) - removes the item at the specified index
# remove() - removes the first occurrence of the item with the specified value

text = "a b c some other text with a b c in it"
pattern = "a\s*b\s*c"  # This regex allows for any spaces between a, b, and c
cleaned_text = re.sub(pattern, "", text) # This will remove all occurrences of "a b c" from the text, regardless of the number of spaces between the letters.

print(cleaned_text)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)

list2 = list1.copy() # copies the list
print(list2)

list3 = list(list1) # copies the list
print(list3)

# You cannot copy list1 by simply assigning it to another variable. If you do so, any changes made to the new list will also affect the original list.
# This is because both lists will point to the same memory location. To create a copy of the list, you can use the copy() method or the list() function.

list1.append(11) # adds an element to the end of the list
print(list1)

# list((1, 2, 3, 4, 5)) # converts a tuple to a list
# list("hello") # converts a string to a list
# tuple([1, 2, 3, 4, 5]) # converts a list to a tuple
# tuple("hello") # converts a string to a tuple
# str([1, 2, 3, 4, 5]) # converts a list to a string

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# for loop - iterates over a sequence (list, tuple, dictionary, set, or string)
# for each - iterates over a sequence and returns the elements one by one

list_112 = [1, 2, 3, 4, 5]
list_113 = ["A", "B", "C", "D", "E"]
for x in list_112:
    print(x)
    for y in list_113:
        print(y)

# range() - generates a sequence of numbers
# range(start, stop, step) - generates a sequence of numbers starting from 'start', up to 'stop' (exclusive), incrementing by 'step'

training_dictionary = {} # creates an empty dictionary
training_dictionary["name"] = "John" # adds a key-value pair to the dictionary
training_dictionary["age"] = 30 # adds a key-value pair to the dictionary
training_dictionary["city"] = "New York" # adds a key-value pair to the dictionary
# training_dictionary.clear() # removes all elements from the dictionary
# del training_dictionary["age"] # removes the key-value pair with the specified key
for key in training_dictionary: # iterates over the keys of the dictionary
    print(key) # prints the keys of the dictionary
    print(training_dictionary[key]) # prints the values of the dictionary
print(training_dictionary) # prints the dictionary
print(training_dictionary.keys()) # prints the keys of the dictionary
print(training_dictionary.values()) # prints the values of the dictionary
training_dictionary[key] = "Updated Value" # updates the value of the specified key]

test_Val = {
    "Set_1": [4, -1, 5, 9, 34, 54, 2]
}
max_value = max(test_Val["Set_1"]) # returns the largest value
print(max_value)