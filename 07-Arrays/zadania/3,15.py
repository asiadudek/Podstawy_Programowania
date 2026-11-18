#Napisz program, który drukuje krotkę (10,20,30,40,50) w odwrotnej kolejności

numbers = (10,20,30,40,50)

print("Tuple:",end=" ") #wypisanie elementow z krotki po przecinku
for x in numbers:
    print(x, end=",")

print() #przejscie do nowej linii

for i in range(len(numbers)): #i to numer pozycji, len(numbers) to liczba elementow
    print(numbers[i], end="") #wypisujemy nasza cyfre
    if i < len(numbers) - 1: #jesli pozycja jest mniejsza od ostatniej pozycji cyfry
        print(",", end="") #to wypisujemy miedzy cyframi przecinek


