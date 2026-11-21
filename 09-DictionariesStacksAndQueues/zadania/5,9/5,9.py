# Napisz program, który oblicza i drukuje, ile zarejestrowanych samochodów pochodzi z każdej prowincji Polski.
#Wykaz prowincji i odpowiadające im pierwsze litery numerów rejestracyjnych pojazdów znajdują się w aktach province.csv

import csv


provinces = {} #litera tablicy -> nazwa wojewodztw
counts = {}  #litera tablicy -> liczba samochodów

with open('province.csv', 'r', encoding = "UTF-8") as file:
    next(file) #pomijamy naglowek
    for line in file:
        fields = line.strip().split(',') #usuwa nam spacje, enter itd(biale znaki) oraz wydziela nam slowa w miejscu przecinka
        provinces[fields[0]] = fields[1] #to jest to samo co np person[key] = value
print(provinces) #fields[0] to litera, fields[1] to nazwa prowincji


with open('vehicle.txt', 'r') as file:
    for line in file:
        plate = line.strip() #nasza tablica jest w wierszu calym czyli calej linijce, usuwamy spacje
        letter = plate[0] #litera tablicy znajduje sie na pierwszym miejscu
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
print(counts) #wypisuje slownik z liczbami samochodow

for letter in counts:
    print(provinces[letter], counts[letter])