#Utwórz funkcję transpose_matrix(m) zwracającą transponowaną macierz m
#Następnie utwórz program, który drukuje transponowane macierze w wierszach i kolumnach dla następujących macierzy.
def transpose_matrix(m):
    result = [] #nasz pusta lista, tutaj będzie macierz transponowana
    for j in range(len(m[0])): # m[0] to pierwszy wiersz macierzy a jego dlugosc to liczba kolumn, wszystkie wiersze maja tyle samo elementow wiec wystarczy jak zmierzymy jeden
        row = [] #pusty wiersz     #Zmienna j to po kolei numery kolumn starej macierzy (0, 1, 2...). Każda stara kolumna stanie się teraz nowym wierszem.
        for i in range(len(m)): #i to numer wiersza macierzy. len(m) to liczba wierszy starej macierzy, pętla przechodzi po wszystkich wierszach starej macierzy.
            row = row + [m[i][j]] #Program bierze element z wiersza i oraz kolumny j ze starej macierzy i dokleja go do naszego nowego wiersza (row). Idzie z góry do dołu po starej kolumnie i układa te liczby od lewej do prawej w nowym wierszu.
        result = result + [row]     #Idzie z góry do dołu po starej kolumnie i układa te liczby od lewej do prawej w nowym wierszu.
    return result
    

def print_matrix(m):
    for row in m: #row to kolejny wiersz macierzy
        for value in row: #wartosc w wierszu
            print(value, end=" ")
        print()

a = [[1, 2, 3],                        
     [4, 5, 6],
     [7, 8, 9]]

b = [[1, 2, 3, 4, 5],                  
     [6, 7, 8, 9, 0]]

c = [[5, 6, 7, 8]] 

print_matrix(transpose_matrix(a))
print()
print_matrix(transpose_matrix(b))
print()
print_matrix(transpose_matrix(c))

