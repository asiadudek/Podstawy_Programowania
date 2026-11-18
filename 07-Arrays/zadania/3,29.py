#funkcja create_2d_arr(x,y) tworzy i zwraca dwuwymiarową tablicę o wartościach 0.
#utwórz dwuwymiarową tablicę o wymiarach 3 na 5
def create_2d_arr(x,y):
    arr = [] #tablica, narazie pusta
    for i in range(x): #i jest licznikiem wierszy, x to nasza liczba wierszy czyli 3
        row = [] #nowy wiersz, narazie pusty
        for j in range(y): #j jest kolumna, y mowi nam ile mamy kolumn czyli 5. Petla wykona sie 5 razy
            row = row + [0] #doklejamy zera do wiersza
        arr += [row] #doklejamy wiersz do tablicy
    return arr

array = create_2d_arr(3,5) #tablica 3x5

for row in array:
    for value in row: #value to liczba w wierszu
        print(value, end="")
    print()