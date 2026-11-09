###
# A program that calculates the number of characters
# of your name, surname and full name
#

name = 'Anna'   # replace Anna with your name
surname = 'May' # replace May with your surname
name_surname = name + " " + surname
characters_in_name = len(name) #len służy do sprawdzenia dlugosci znakow (liter)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} charakters')
print(f'Your full name has {len(name_surname)} charakters') # with a space between name and surname