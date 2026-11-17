###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#

import my_keyboard 

first_name = my_keyboard.input_string("Enter first name: ")
last_name = my_keyboard.input_string("Enter last name: ")
age = my_keyboard.input_integer("Enter an age: ")
salary = my_keyboard.input_real("Enter a salary: ")
is_salary_hidden = my_keyboard.input_boolean("Hide salary? (y/n): ")

print('DATA RECORD')
print('===========')
print("Name: ",first_name)
print("Last name: ",last_name)
print("Age: ",age)
if not is_salary_hidden:
    print("Salary: ",salary)