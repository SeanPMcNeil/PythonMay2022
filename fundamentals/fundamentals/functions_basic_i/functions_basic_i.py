#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# will print "5" because of the <return 5> in the function that is called

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# give an error because the first function is not defined before calling it


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# will print "5" because it is the first return the function reaches, ending the function

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# will print 5 because the function returns that value and ends before printing 10

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# will print 5 once, then print none because the function does not return a value

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# will pring 3, then 5 - then gives an error because the function does not return a value to be used in the final line

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# will print "25" because it changes 2 and 5 to strings and concatenates them 

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# will print 100, then 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# will print 7, then 14, then 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# will print 8 because the function returns the value and ends

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# will print 500, then 500, then 300, then 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# will print 500, then 500, then 300, then 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# will print 500, then 500, then 300, then 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# will print 1, then 3, then 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# will print 1, then 3, then 5, then 10