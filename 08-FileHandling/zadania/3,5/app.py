###
# Checks the correctness of username and password
#Napisz program, który sprawdza, czy nazwa użytkownika i hasło wprowadzone z klawiatury spełniają poniższe wymagania. Używaj wyrażeń regularnych.
import re

# read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# pattern (criteria) for username and password

# Wzorce (kryteria) dla nazwy użytkownika i hasła
# r'...' - "surowy" napis, dzięki niemu Python nie psuje znaków specjalnych jak \w
# ^  - początek tekstu
# [a-z] - jedna mała litera od a do z
# {6,}  - poprzedni element ma wystąpić co najmniej 6 razy (bez górnego limitu)
# $  - koniec tekstu
# Razem: nazwa składa się WYŁĄCZNIE z małych liter a-z i ma min. 6 znaków
username_pattern = r'^[a-z]{6,}$'


# \w  - dowolna litera, cyfra lub podkreślenie 
# {8,} - co najmniej 8 takich znaków
# Razem: hasło składa się WYŁĄCZNIE z liter, cyfr lub _ i ma min. 8 znaków
password_pattern = r'^\w{8,}$'

# check if username and password are ok
username_match = re.findall(username_pattern, username) #zwraca liste znalezionych dopasowań
password_match = re.findall(password_pattern, password)

# print results
if username_match and password_match:
   print("Username and password are correct")
else:
   print("Username or password is incorrect")