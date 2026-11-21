#Napisz program, który drukuje informacje podsumowujące, jak podano poniżej. Podziel program na mniejsze części definiujące funkcje.
#liczba pokoi
#liczba opłaconych rezerwacji
#liczba niezapłaconych rezerwacji
#łączna wartość opłaconych rezerwacji
#łączna wartość niezapłaconych rezerwacji


import json #modul do odczytywania i zapisu plikow json


def load_reservations(filename): #Funkcja wczytuje plik i zwraca liste rezerwacji
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file) 
    return data['reservations'] 


def count_rooms(data):
    rooms = [] # lista numerów pokoi, które już widzieliśmy
    for reservation in data:
        if reservation['room_number'] not in rooms: #jeśli tego pokoju jeszcze nie ma na liście
            rooms.append(reservation['room_number']) #dopisujemy go
    return len(rooms) #liczba różnych pokoi = długość listy


def count_paid(data): 
    count = 0 #licznik rezerwacji oplaconych, narazie jest 0
    for reservation in data:
        if reservation['paid'] == True: #jesli pole paid jest true to zwiekszamy licznik
            count += 1
    return count


def count_unpaid(data):
    count = 0 #licznik rezerwacji nieplaconych
    for reservation in data:
        if reservation['paid'] == False:
            count += 1
    return count


def value_paid(data): #funkcja sumuje wartosc rezerwacji oplaconych
    total = 0
    for reservation in data:
        if reservation['paid'] == True:
            total += reservation['price_per_night']
    return total


def value_unpaid(data):
    total = 0
    for reservation in data:
        if reservation['paid'] == False:
            total += reservation['price_per_night']
    return total


data = load_reservations('reservations.json') 

print("Liczba pokoi:", count_rooms(data))
print("Liczba opłaconych rezerwacji:", count_paid(data))
print("Liczba niezapłaconych rezerwacji:", count_unpaid(data))
print("Łączna wartość opłaconych rezerwacji:", value_paid(data))
print("Łączna wartość niezapłaconych rezerwacji:", value_unpaid(data))