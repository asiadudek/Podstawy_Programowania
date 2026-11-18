#Tablica zawiera wartości: 15, 8, 31, 47, 2, 19. Utwórz program, który oblicza i drukuje tablicę oraz średnią arytmetyczną wartości tablicy. Użyj instrukcji pętli “for”.
arr = [15, 8, 31, 47, 2, 19]

result = 0 #nasze miejsce gdzie bedzie przechowywana suma


for value in arr:
    result += value

average = result / len(arr)

print("Array: ", arr)
print("Average;",round(average,2))