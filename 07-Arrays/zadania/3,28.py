#Utwórz program, który oblicza sumę wartości w ostatniej kolumnie.
array = [[7, 3, 7, 9, 0],                
         [2, 9, 0, 1, 5],
         [3, 8, 6, 4, 7],
         [8, 7, 1, 1, 5]]

total = 0 #nasza suma, narazie wynosi 0
for row in array: #nasz caly wiersz
    total += row[4] #row[4] to pozycja naszego ostatniego elementu w danym wierszu, wszystkie elementy na ostatnim miejscu w wierszach sumujemy

print(total)