###
# Checks the correctness of username and password
#Napisz program, który sprawdza, czy nazwa użytkownika i hasło wprowadzone z klawiatury spełniają poniższe wymagania. Używaj wyrażeń regularnych.
#nazwa użytkownika ma długość co najmniej 6 znaków
#nazwa użytkownika zawiera tylko małe litery
#hasło ma co najmniej 8 znaków
#hasło zawiera tylko litery (małe i wielkie), cyfry i znak podkreślenia


import re

# read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# pattern (criteria) for username and password

username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^\w{8,}$'

# check if username and password are ok
username_match = re.findall(username_pattern, username) #zwraca liste znalezionych dopasowań
password_match = re.findall(password_pattern, password)

# print results
if username_match and password_match:
   print("Username and password are correct")
else:
   print("Username or password is incorrect")