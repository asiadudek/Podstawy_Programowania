#Tablica zawiera wartości: 15, 8, 31, 47, 2, 19. Utwórz program, który oblicza i drukuje tablicę oraz średnią arytmetyczną wartości tablicy. Użyj instrukcji pętli “while”.
arr = [15, 8, 31, 47, 2, 19]

result = 0 #nasze miejsce gdzie bedzie przechowywana suma, narazie jest pusta
i = 0 #nasz licznik, czyli numer aktualnego elementu listy

while i < len(arr): #petla bedzie wykonywac sie dopoki pozycja elementu jest mniejsza niz calkowita dlugosc tablicy
    result += arr[i] #dodajemy aktualny element z tablicy do sumy
    i += 1 #po dodaniu zwiekszamy nasza pozycje, przesuwamy sie w prawo do kolejnego elementu

average = result / len(arr) #srednia arytmetyczna czyli suma podzielona na ilosc elementow tablicy

print("Array: ", arr)
print("Average;",round(average,2))