# sample function
# accept a list of integers as its input
# output a new list consisting of only positive integers

# The "Like JS" Method
# def sample_function_name(input_list):
#     output_list = []

#     for i in range(0, len(input_list)):
#         if input_list[i] >= 0:
#             output_list.append(input_list[i])

#     return output_list

# print(sample_function_name([1, -3, 9, -2, 7]))

# The "Better" Method
def sample_function_name(input_list):
    output_list = []

    for number in input_list:
        if number >= 0:
            output_list.append(number)
    return output_list

print(sample_function_name([1, -3, 9, -2, 7]))

# def every_third_item(input_list):

#     for i in range(0, len(input_list), 3):
#         print(input_list[i])

# every_third_item(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

def every_third_item(input_list):

    for item in input_list[::3]:
        print(item)

every_third_item(['a', 'b', 'c', 'd', 'e', 'f', 'g'])