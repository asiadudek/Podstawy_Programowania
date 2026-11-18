#Napisz program oddzielający liczby parzyste i nieparzyste danej tablicy liczb całkowitych. 
#Najpierw umieść wszystkie liczby parzyste, a potem liczby nieparzyste.

arr = [7, 9, 2, 4, 5, 6]
#tablica wyjsciowa
print("Arr = ", end="") #wypisujemy tablice przed zmiana

result = []#puste miejsce na nowa tablice

for x in arr: #przeszukujemy liczby w naszej tablicy, szukamy najpierw parzystych
    if x % 2 == 0:
        result = result + [x] #x w nawiasie bo dopisujemy to na koniec do naszej tablicy

for x in arr: #teraz szukamy liczb nieparzystych
    if x % 2 == 1:
        result = result + [x] #dopisujemy na koniec naszej tablicy liczbe nieparzysta

print("Arr = ", result)



