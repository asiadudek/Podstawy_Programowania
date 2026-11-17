# Zdefiniuj funkcję, która zwraca wartość True, jeśli w pokoju znajdowały się jednocześnie co najmniej 3 osoby, lub False w przeciwnym wypadku
# + osoba wchodzaca do pokoju
# - osoba wychodzaca z pokoju
def f(detector):
    in_room = 0 #licznik osob ktore wchodza do pokoju
    for sign in detector: #przeszukujemy kazdy znak w naszym detektorze
        if sign == "+":
            in_room += 1 #zwiekszamy nasz licznik osob o 1
        else:
            in_room -= 1 #zmniejszamy nasz licznik osob o 1
        if in_room >= 3:
            return True
    return False

detector = input("Enter detector: ")
print("Detector:",detector)
print(f(detector))