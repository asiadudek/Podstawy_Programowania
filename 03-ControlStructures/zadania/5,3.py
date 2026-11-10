###
# Prints a greeting
#
name = '' #zmienna przechowujaca nasze imie, narazie jest pusta

while name == '': #petla bedzie sie wykonywac dopoki zmienna "name" jest pusta
    name = input("Enter your name: ") #pobieramy imie od uzytkownika. Trafia ono do zmiennej "name"

print(f"Hello {name}")