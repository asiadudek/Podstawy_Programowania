#Napisz program, który zlicza liczbę wystąpień dowolnej wartości z krotki. 
numbers = (50,20,40,50,30,50)

print("Tuple ",end="")

for i in range(len(numbers)): #i to numer pozycji, len(numbers) to ilosc elementow
    print(numbers[i], end="") #wypisujemy element z pozycji i bez przejscia do nowej linii
    if i < len(numbers) - 1: #jesli nasza pozycja jest mniejsza niz pozycja ostatniego elementu
        print(",", end="") #wypisujemy przecinek, tak aby na koncu go nie bylo
print()

value = int(input("Enter value: ")) #podajemy jakas wartosc, liczbe zeby sprawdzic ile razy wystepuje ona w krotce

counter = 0 #licznik powtorzen liczby
for x in numbers: #przeszukujemy kazda liczbe w naszej krotce
    if x  == value: #jesli liczba z krotki jest taka sama jak liczba podana z klawiatury
        counter += 1 #zwiekszamy licznik o 1

print("Numbers of occurrences: ",counter) #licznik powtorzen