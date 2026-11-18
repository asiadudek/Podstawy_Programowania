#Dwuwymiarowa tablica o wymiarach 2 na 4 zawiera liczby całkowite. 
#utwórz program, który drukuje wartości tablicowe w wierszach i kolumnach.
array = [[1, 2, 3, 4],                   # array = tablica 2D
         [5, 6, 7, 8]]



for row in array:
    for value in row:
        print(value, end=" ")
    print()