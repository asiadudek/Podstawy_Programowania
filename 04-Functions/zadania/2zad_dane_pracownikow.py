###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#

import keyboard # type: ignore

first_name = keyboard.input_string("Enter first name: ")
last_name = keyboard.input_string("Enter last name: ")
age = keyboard.input_integer("Enter an age: ")
salary = keyboard.input_integer("Enter a salary: ")
is_salary_hidden = keyboard.input_boolean("Hide salary? (y/n): ")

print('DATA RECORD')
print('===========')
print("Name: ",first_name)
print("Last name: ",last_name)
print("Age: ",age)
if not is_salary_hidden:
    print("Salary: ",salary)