#Utwórz funkcję, która konwertuje tablicę dwuwymiarową (2 D) na 1 D. 
#Następnie utwórz program, który drukuje tablicę 1 D dla następujących tablic 2 D.
a = [[2, 3], [1, 5]]
b = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]
c = [[2, 1], [3, 5], [7, 4], [2, 6]]


def change(m):
    result = [] #pusta tablica
    for row in m: #pętla przechodzi po każdym wierszu w tablicy m
        for value in row: #pętla przechodzi po każdej wartości w wierszu
            result = result + [value] #dodajemy aktualną wartość do naszej nowej tablicy
    return result #zwraca nasza nowa tablice

def print_matrix(l): #lista 1D do wypisania powstala w funkcji wyzej
    for value in l: #przechodzimy po każdej wartości
        print(value, end=" ") #wyswietlamy kazda wartosc w jednej linii
    print()

print_matrix(change(a))
print()
print_matrix(change(b))
print()
print_matrix(change(c))