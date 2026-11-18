#Utwórz program, który modyfikuje wartości tablicy, aby utworzyć tabliczkę mnożenia, jak poniżej. Użyj instrukcji pętli.
values = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

for i in range(5): #i to numer wiersza, petla wykona sie 5 razy
    for j in range(5): #j to numer kolumny, petla wykona sie 5 razy
        values[i][j] = (i+1)*(j+1) #indeksy zaczynaja sie od 0 a tabliczka mnozenia od 1 dlatego je zwiekszamy

for row in values: #przeszukujemy wiersz w danej tablicy
    for value in row: #przeszukujemy wartosci w naszym wierszu
        if value < 10: #liczba jednocyfrowa jest wezsza niz dwucyfrowa
            print(" ",end="") #dodajemy spacje aby kolumny byly dobrze wyrownane
        print(value, end=" ") #wypisujemy liczbe i spacje bez nowej linii
    print()
