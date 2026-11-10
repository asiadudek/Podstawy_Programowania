###
# Checking login and password
#

login = "joe"
password = "abc"
entered_login = input("Enter your login: ")
entered_password = input("Entered password: ")

if entered_login == login and entered_password == password:
    print("You are logged in.")
else:
    print("Incorrect login or password!")