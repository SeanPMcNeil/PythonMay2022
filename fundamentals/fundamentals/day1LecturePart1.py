x = 3
y = 7
# declaring variables, no ; needed, no keyword needed
print(x + y)
# logging statement

z = 3.14159 # float is different from an integer | floats are numbers with a decimal
# numbers like 3.00 are still floats

sample_list = [5, 7, 19, -8] # similar to an array in JS but behaves a little different
# list = a collection of data in a given order

print(sample_list[0]) # access items in lists like in arrays in JS
print(sample_list[-1]) # giving negative values will wrap to the end of the array
# print(sample_list[-5]) # gives Index Error | tells you that there is no value at the location you're looking at

# None = null -> same "value" need the capitalization
# True | False -> need to be capitalized to use these values in Python

dog = ('Bruce', 'cocker spaniel', 19, False) # tuple is a list that you cannot modify | not super common

new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# dictionaries are similar to Objects in JS, still referred to as keys and values
print(new_person['name'])

x = 3
if x == 3:
    print('x is equal to three :)')
else:
    print('x is not equal to three :(')
# the indentation is necessary in order for the interpreter to know what code goes where
# will get an Indentation Error if you are inconsistent with it
# Tabs and spaces can be different depending on the editor - you can use tabs or spaces, but not both!

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

from lzma import _OpenBinaryWritingMode
import random
from turtle import right
print(random.randint(2,5)) # provides a random number between 2 and 5

# print will insert a space between elements separated by a comma
name = "Zen"
print("My name is", name)

# or you can concatenate the contents into a new string
print("My name is " + name)

# Python doesn't know how to add a string and a number, but can add two strings together
# You can cast a number as a string
print("Hello" + str(42))

# Can inject variables into our strings | String Interpolation
# f-strings
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")
# string.format()
# Type out the full string with {} where it will pull values from variables
# Then call the format method on the string, passing in values in order that they should appear
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

# %-formatting
# % used as a placeholder | %s for a string, %d for a number
# after the string, a single % separates the string to be interpreted
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

# Built-in String Methods
x = "hello world"
print(x.title())
# output:
"Hello World"

# Other common string methods

# string.upper(): returns a copy of the string with all the characters in uppercase.
# string.lower(): returns a copy of the string with all the characters in lowercase.
# string.count(substring): returns number of occurrences of substring in string.
# string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

# elements inside a list do not need to be the same data type
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

# append a list
# your_list.append(sone_new_element)

x = [1,2,3,4,5]
x.append(99)
print(x)
# the output would be [1,2,3,4,5,99]

# Python uses [] to return a copy of a list, constrained to specific indices, non-inclusive of the final index included
x = [99,4,2,5,-3]
print(x[:])
# the output would be [99,4,2,5,-3]
print(x[1:])
# the output would be [4,2,5,-3];
print(x[:4])
# the output would be [99,4,2,5]
print(x[2:4])
# the output would be [2,5];

# Built-in list functions
# len(sequence): Returns the number of items in a sequence
# enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
# map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence

# Built-in list Methods
# list.append(value)
# list.extend(list2) adds all values from a second sequence to the end of the original sequence.
# list.pop(index) remove a value at given position. if no parameter is passed, defaults to final value in the list.
# list.index(value) returns the index position in a list for the given parameter.

# Built in Tuple Functions
# len(sequence): Returns the length of the given tuple.
# max(sequence) returns the largest value in the sequence
# sum(sequence) return the sum of all values in sequence
# enumerate(sequence) used in a for-loop context to return two-item-tuple for each item in the sequence indicating the index followed by the value at that index.
# map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence

# functions can only return a single value but by making that value a tuple we can
# group together as many values as we like, and return them together

# a dictionary:
# - is an unordered collection of objects
# - values are accessed using a key
# - can shrink or grow as needed
# - the contents can be modified
# - can be nested
# - sequence operations like slice cannot be used with dictionaries

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

# keys must be unique | if you make an assignment using an existing key the old value is overwritten
# accessing values
print(weekend["Sun"])
print(capitals["svk"])

# removing values
value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything


# Nested Dictionaries | can contain lists and tuples
context = {
    'questions': [
        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}

#Built-in Functions and Methods
# cmp(dict1, dict2) - Compares two dictionaries. The comparison process starts with the length of each dictionary, followed by key names, followed by values. The function returns 0 if the two dicts are equal, -1 if dict1 > dict2, 1 if dict1 < dict2.
# len() - give the total length of the dictionary.
# str() - produces a string representation of a dictionary.
# type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dict type.

# (either dict.method(yourDictionary) or yourDictionary.method() will work)

# .clear() - removes all elements from the dictionary
# .copy() - returns a shallow copy dictionary
# .fromkeys(sequence, [value] ) - create a new dictionary with keys from sequence and values set to value.
# .get(key, default=None) - For key key, returns value or default if key is not in dictionary.
# .items() - returns a list of dictionary's (key, value) tuple pairs.
# .keys() - return a list of dictionary keys.
# .setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
# .update(dict2) = adds dictionary dict2's key-values pairs to an existing dictionary.
# .values() - returns list of dictionary values.

# Conditionals
x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false   

# Comparison & Logic Operators
# ==  - checks if the value of two operands are equal
# !=  - checks if the value of two operands are not equal
# >   - checks if the value of the left is greater than the value of the right
# <   - checks if the value of the left is less than the value of the right
# >=  - checks if the value of the left is greater than or equal to the value of the right
# <=  - checks if the value of the left is less than or equal to the value of the right
# and - checks that each expression on the left and right are both True
# or  - checks if either expression on the left or right is True
# not - reverses the true-false value of the operand

# For Loops with Range
# can have between 1 and three arguments
# 1 argument | Start: Defaults to 0; Stop: Exclusive of 1st; Step: Defaults to 1
# 2 arguments | Start: inclusive of 1st; Stop: Exclusive of 2nd; Step: Defaults to 1
# 3 arguments | Start: inlcusive of 1st; Stop: Exclusive of 2nd; Step: iterates by 3rd
# if you need to specify an increment other than +1 all 3 arguments are required

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# For Loops through Strings
# can access each value of a string individual with a loop

for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'

# For Loops through Lists
# can use the range function and send the length of teh list as a stopping value
# can also loop to get the values of the list directly

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

# For Loops through Tuples
# can iterate through a tuple like a list

for data in dog:
    print(data)

# For Loops through Dictionaries
# the iterator is each of the keys of the dictionary

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# While Loops
# loop while a certain condition is true

count = 0
while count < 5:
    print("looping - ", count)
    count += 1

# while <expression>:
    # do something, including progress towards making the expression False. 
    # Otherwise we'll never get out of here!

# Else
# used to still perform an action if the condition was not met in a while loop

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

# Loop Control
# Break: exits the current loop prematurely, resuming execution at the first post-loop statement
#   used in both for and while loops
#   when loops are nested, a break will only exit from the innermost loop

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

# Continue: immediately returns control to the beginning of the loop
#   rejects, or skips, all of the remaining statements in the current iteration of the loop
#   and continues normal execution of the loop

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1

