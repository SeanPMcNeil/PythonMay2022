num1 = 42 # variable declaration, initialize integer
num2 = 2.3 # variable declaration, initialize float
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) # log statement, type check, <class 'tuple'>
print(pizza_toppings[1]) # log statement, access 2nd value of pizza_toppings list
pizza_toppings.append('Mushrooms') # add value 'Mushrooms' to end of pizza_toppings list
print(person['name']) # log statement, access 'name' value of person dictionary
person['name'] = 'George' # change value of 'name' value inside person dictionary from 'John' to 'George'
person['eye_color'] = 'blue' # add value 'eye_color': 'blue' to person dictionary
print(fruit[2]) # log statement, access 3rd value of fruit tuple

if num1 > 45: # conditional: if
    print("It's greater") # log statement if conditional is true
else: # conditional: else
    print("It's lower") # log statement if first conditional is false (it is)

if len(string) < 5: # conditional: if, length check of var string
    print("It's a short word!") # log statement if conditional is true
elif len(string) > 15: #conditional: else if, length check of var string
    print("It's a long word!") #log statement if first conditional is false and else if statement is true
else: # consitional: else
    print("Just right!") # log statement if both conditionals above are false (they are)

for x in range(5): # for loop start, increment numbers for a range of 5 (non-inclusive)
    print(x) # log statement (logs 0, 1, 2, 3, 4, 5)
for x in range(2,5): # for loop start, increment numbers in a range from 2 to 5 (non-inclusive)
    print(x) # lof statement (logs 2, 3, 4)
for x in range(2,10,3): # for loop start, increment numbers in a range from 2 to 10 (non-inclusive) by 3
    print(x) # log statement (logs 2, 5, 8)
x = 0 # variable declaration, initialize integer
while(x < 5): # while loop start
    print(x) # log statement (logs 0, 1, 2, 3, 4)
    x += 1 # while loop increment

pizza_toppings.pop() # list delete value, removes element at the last index of the list pizza_toppings
pizza_toppings.pop(1) # list delete value, removes element at index 1 (the second element) of the list pizza_toppings

print(person) # log statement, access person dictionary
person.pop('eye_color') # dictionary delete value, remove 'blue' and 'eye_color' from person dictionary
print(person) # log statement, access person dictionary (logs {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False})

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': # conditional: if
        continue # for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': # conditional: if
        break #for loop break

def print_hello_ten_times(): # function definition
    for num in range(10): # for loop
        print('Hello') # log statement

print_hello_ten_times() # call/run function

def print_hello_x_times(x): # function definition, variable declaration
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # call/run function, pass in parameter 4 for x

def print_hello_x_or_ten_times(x = 10): # function definition, variable declaration, 
    for num in range(x): # for loop
        print('Hello')# log statement

print_hello_x_or_ten_times() # call/run function with default parameter x = 10
print_hello_x_or_ten_times(4) # call/run function, pass in parameter 4 for x


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 # variable declaration, initialize integer
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'