#Utwórz moduł MyArrays zawierający funkcje do działania na tablicy liczb:

#Funkcja zwracająca drugi co do wielkości element tablicy
#Funkcja zwracająca różnicę między największą i najmniejszą wartością w tablicy
#Funkcja zwracająca medianę liczb w tablicy.
#Nie używaj wbudowanych funkcji. Mediana jest wartością środkową w uporządkowanym ciągu liczb:
#Funkcja zwracająca dwuelementową tablicę zawierającą najmniejsze i największe wartości w tablicy

#Funkcja zwracająca elementy tablicy jako ciąg znaków, oddzielone znakiem minus

import MyArrays

numbers = [7,3,8,5,2]

print("Numbers: ", end="")  # end="" = nie przechodź do nowej linii
for i in range(len(numbers)):
    print(numbers[i], end="")
    if i < len(numbers) - 1:
        print(",", end="")
print()  # pusty print = przejście do nowej linii

#Funkcje z modułu wywołujemy z nazwą modułu: MyArrays.nazwa_funkcji
print("Second largest number:", MyArrays.second_largest(numbers))
print("Median:", MyArrays.median(numbers))

#Funkcja zwraca listę [najmniejsza, największa]
result = MyArrays.smallest_and_largest(numbers)  # zapisujemy ją w zmiennej
print("Smallest and largest number: ", end="")
print(result[0], end=",")  # result[0] = najmniejsza
print(result[1])           # result[1] = największa

#Funkcja zwraca gotowy napis
print("Numbers as a string:", MyArrays.to_string(numbers))
