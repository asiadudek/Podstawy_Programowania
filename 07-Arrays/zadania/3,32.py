#Dwuwymiarowa tablica o wymiarach 3 na 5 zawiera liczby całkowite. 
#Utwórz program, który zamienia pierwszy i ostatni wiersz.

array = [[1, 2, 3, 4, 5],             
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15]]


#Tablica przed zmiana
for row in array:
    for value in row:
        print(value,end=" ")
    print()
    
#Tablica po zmianie
array[0], array[2] = array[2], array[0]

print()

for row in array:
    for value in row:
        print(value, end=" ")
    print()
    