###
# A program that checks whether the password length
# read from the keyboard is correct.
#

password = input("Enter your password: ")
password_ok = len(password) >= 8
print(f"Password length is valid: {password_ok}") #dlugosc hasla jest prawidlowa