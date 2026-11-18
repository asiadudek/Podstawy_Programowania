#Utwórz program, który zastępuje wartości głównej przekątnej wartością 1. Użyj instrukcji pętli. Wydrukuj zmodyfikowaną tablicę.

matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range(len(matrix)): #i to pozycja danego elementu macierzy, len(matrix) to ilosc elementow macierzy
    matrix[i][i] = 1 #wiersz i, kolumna i, zamieniamy na 1

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()