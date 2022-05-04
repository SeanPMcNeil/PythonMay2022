# OOP (Object Oriented Programming) is a big deal
# Most languages you use as a modern developer are object oriented
# Using objects effectively comes down mostly to experience
# OOP is the binding of data and associated behavior

# employees = []

# employees.append({'first_name': 'Alex', 'last_name': 'Smith', 'salary': 87000})
# employees.append({'first_name': 'Bradley', 'last_name': 'Jones', 'salary': 62000})
# employees.append({'first_name': 'Charlie', 'last_name': 'Adams', 'salary': 89000})

# # employees.append({'first_name': 'David', 'last_name': 'Jones', 'salary': '73000'})
# # this gives us problems because we expect the salary data to be stored as an integer and not a string
# employees.append({'first_name': 'David', 'last_name': 'Jones', 'salary': 73000})

# # another new employee
# # employees.append({'first_name': 'Eeeeee', 'last_name': 'Smith', 'salry': 98000})
# # give an error later because the 'salary' key is stored incorrectly
# employees.append({'first_name': 'Eeeeee', 'last_name': 'Smith', 'salary': 98000})

# # another another new employee
# employees.append({'first_name': 'Francis', 'last_name': 'Alexander', 'salary': 82000})


# print("Increasing salary...")
# for employee in employees:
#     employee['salary'] = employee['salary'] * 1.05
#     # employee['salary'] = employee['salary'] * 105
#     # this is too much and would cause problems if we were using it to calculate raises

# print("After increase:")
# for employee in employees:
#     print(f"First name: {employee['first_name']}, Last name: {employee['last_name']}, Salary: {employee['salary']}")

class Employee():
    def __init__(self, first_name, last_name, salary, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary
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


# when you create employees from this class, they are known as "instances" of the class
employee_1 = Employee("Alex", "Smith", 82000)
employee_2 = Employee("Bradley", "Jones", 79000)
employee_3 = Employee("Charlie", "Adams", 65000)
employee_4 = Employee("Darla", "Smith", 85000, middle_name = "Allison")
employee_5 = Employee("Eric", "Smith", 40000)

employees = [employee_1, employee_2, employee_3, employee_4, employee_5]

for employee in employees:
    # if employee.middle_name == None:
    #     print(f"Full Name: {employee.first_name} {employee.last_name}, Salary: {employee.salary}")
    # else:
    #     print(f"Full Name: {employee.first_name} {employee.middle_name} {employee.last_name}, Salary: {employee.salary}")
    print(f"Full Name: {employee.full_name()}, Salary: {employee.salary}")

print("-" * 20)

# for employee in employees:
#     # employee.salary = employee.salary * 1.05 # DON'T DO THIS
#     # call a method to change salary
#     employee.change_salary(5)

# for employee in employees:
#     print(f"Full Name: {employee.full_name()}, Salary: {employee.salary}")

for employee in employees:
    # employee.salary = employee.salary * 1.05 # DON'T DO THIS
    # call a method to change salary
    employee.change_salary(-3)
    # Because we defined the method in the Employee class, this pay cut will not effect employee_5 because they are at the salary floor

for employee in employees:
    print(f"Full Name: {employee.full_name()}, Salary: {employee.salary}")