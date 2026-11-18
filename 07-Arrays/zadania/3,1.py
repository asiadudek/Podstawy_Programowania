#Tablica zawiera liczby całkowite: 34,7,19,4,21,8. Utwórz program, który oblicza i drukuje liczbę parzystych wartości w tablicy.
arr = [34, 7 , 19, 4, 21, 8]
total = 0 #tu bedziemy przechowywac nasza liczbe znalezionych liczb parzystych
i = 0 #indeks od ktorego zaczynamy
while i < len(arr): #petla bedzie sie wykonywac dopoki pozycja naszej sprawdzanej wartosci bedzie mniejsza od calkowitej ilosci elementow tablicy
    if arr[i] % 2 == 0:
        total += 1
    i += 1 #przesuwamy się do nastepnego elementu

print(total)

    