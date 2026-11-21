###
# Reads the entire contents of a file
# Zmodyfikuj program, aby wydrukować listę krajów posortowaną alfabetycznie.

with open('countries.txt', 'r') as file:
    content = file.read()

countries = content.splitlines() #content zwraca nam caly plik, a splitlines wydziela nam linie
sorted_countries = sorted(countries)

for country in sorted_countries:
    print(country)


