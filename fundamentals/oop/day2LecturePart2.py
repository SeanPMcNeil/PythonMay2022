# encapsulation
## the idea that we can group code together into objects
## when the class interacts with and is responsible for it's own data, it implies that other classes should
## not be responsible for that data || if we want that data to be changed/accessed, we typically use
## a method to ask it to (which it replies either yes or no to)

class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")

# inheritance
## the idea that we pass along attributes and methods from one class into a "sub-class" or child class
## and not have to re-write the code to make it work.
## Child classes can be more specific versions of their Parent class. Using the key word "super" will call methods

class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super.brew_now(beans)
        print("Frothy!!!")

# polymorphism
## means "many forms" - a Child class can have a different version of a method from a Parent class
## 2 Classes can have similar methods, but the way those methods happen is a little different

class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super.brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")

# abstraction
## when two objects interact w/ each other, they don't necessarily need to know how they each work
## they just need to be able to rely on those methods working

class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self, beans):
        self.cafe.brew_now(beans)

# Association Between Classes - how they relate to each other or how they can work w/ each other

class Department():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

class Employee():
    def __init__(self, first_name, last_name, salary, department, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary
        self.department = department
        self.department.add_employee(self)
        # each one of these are properties that each instance of Employee will have

    def full_name(self):
        if self.middle_name == None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

    def change_salary(self, percent_increase):
        # the class needs to be responsible for changing the data because it knows what is and isn't valid for that data
        if percent_increase > 10:
            return None
        
        new_salary = self.salary * (1 + (.01 * percent_increase))

        if not new_salary < 40000:
            self.salary = new_salary

    def __repr__(self): # string we can show to the dev to represent the item w/ as little info as possible
        return f"{self.first_name[0]}. {self.last_name}"
        # adds behavior to make it easier for other developers to work with

department_a = Department("Sales", "804a")
department_b = Department("Engineering", "201b")

employee_1 = Employee("Alex", "Smith", 82000, department_a)
employee_2 = Employee("Bradley", "Jones", 79000, department_a)
employee_3 = Employee("Charlie", "Adams", 65000, department_b)
employee_4 = Employee("Darla", "Smith", 85000, department_a, middle_name = "Allison")
employee_5 = Employee("Eric", "Smith", 40000, department_b)

print(employee_1)
print(department_a.employees)
print(department_b.employees)