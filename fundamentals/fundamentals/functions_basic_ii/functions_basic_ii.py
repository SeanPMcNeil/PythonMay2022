# 1. Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(start):
    count = start
    countdown_list = []
    while count >= 0:
        countdown_list.append(count)
        count -= 1
    print(countdown_list)

countdown(5)

# 2. Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.

def print_and_return(num_list):
    print(num_list[0])
    return num_list[1]

return_num = print_and_return([1,2])
print(return_num)

# 3. First Plus Length - 
# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_plus_length(num_list):
    sum = num_list[0] + len(num_list)
    return sum

return_value = first_plus_length([1, 2, 3, 4, 5])
print(return_value)

# 4. Values Greater than Second - Write a function that accepts a list and 
# creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, 
# have the function return False

def values_greater_than_second(num_list):
    new_list = []
    count = 0
    if len(num_list) < 2:
        return False
    for x in num_list:
        if x > num_list[1]:
            new_list.append(x)
            count += 1
    print(count)
    return new_list

result_list = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(result_list)
result_list2 = values_greater_than_second([3])
print(result_list2)

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.

def length_and_value(size, value):
    new_list = []
    for amount in range(0,size):
        new_list.append(value)
    return new_list

x = length_and_value(4, 7)
print(x)
y = length_and_value(6, 2)
print(y)