#Dwuwymiarowa tablica o wymiarach 3 na 5 zawiera liczby całkowite.
#Utwórz program, który zamienia pierwszą i ostatnią kolumnę. Drukuj wartości tablicy w wierszach i kolumnach przed i po zmianach.


array = [[1, 2, 3, 4, 5],              
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15]]


#Przed zmiana
for row in array:
    for value in row:
        print(value,end=" ")
    print()

#Po zmianie
for i in range(len(array)): #i to indeks wiersza, len(array) to liczba wierszy
    array[i][0], array[i][4] = array[i][4], array[i][0]
print()


for row in array:
    for value in row:
        print(value, end=" ")
    print()