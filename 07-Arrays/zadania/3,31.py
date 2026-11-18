#Utwórz program, który znajdzie najmniejsze i największe wartości w tablicy oraz w którym wierszu i kolumnie się one znajdują
array = [[-38, 19], 
        [5,40],
        [-7,11],
        [29,16]]

minimum = 0 #najmniejsza znaleziona wartosc, narazie wynosi 0
maximum = 0 #najwieksza znaleziona wartosc, narazie wynosi 0

for row in array: #przeszukujemy kazdy wiersz w tablicy 
    for value in row: #przeszukujemy kazda wartosc w wierszu
        if value < minimum: #jesli znaleziona wartosc jest mniejsza od naszego przyjetego minimum
            minimum = value #to znalezlismy minimum
        if value > maximum: #jesli wartosc jest wieksza od naszego przyjetego maximum
            maximum = value #to znalezlismy maximum

#sprawdzamy na jakiej pozycji się znajdują
for i in range(len(array)): #i numer wiersza, len(array) to liczba wierszy
    for j in range(len(array[i])): #j numer kolumny, len(array[i]) to dlugosc konkretnego wiersza czyli il kolumn
        if array[i][j] == minimum: 
            print("Minimum is:",minimum,",row:",i,",column",j)
        if array[i][j] == maximum:
            print("Maximum is: ",maximum,",row:",i,",column",j)