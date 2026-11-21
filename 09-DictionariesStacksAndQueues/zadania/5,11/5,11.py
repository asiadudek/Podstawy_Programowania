#Program pobiera imię i nazwisko danej osoby z klawiatury i zwiększa liczbę głosów na tę osobę o 1.
#Jeśli jest to nowa osoba, jest ona dodawana do listy z liczbą głosów równą 1.

import json


with open('voting.json', 'r', encoding = 'UTF-8') as file:
    votes = json.load(file) #ladujemy zawartosc pliku do slownika imie - liczba glosow

# Vote for a person
person_name = input('Name of the person you are voting for: ')
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

# Save voting data to json file
with open('voting.json', 'w', encoding = 'UTF-8') as file:
    json.dump(votes, file) #zapisujemy zaaktualizowany slownik z powrotem do pliku