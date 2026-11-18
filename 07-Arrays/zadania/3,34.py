#utwórz funkcję, która drukuje tablicę 2 D w wierszach i kolumnach. 
#Na koniec utwórz program, który drukuje trzy macierze tożsamości o wymiarach 3, 5 i 8
def identity_matrix(n): #macierz kwadratowa, n - liczba kolumn i wierszy
    result = [] #nasza macierz
    for i in range(n): #i to numer wiersza, jeden obrot = 1 wiersz
        row = [] #nowy wiersz
        for j in range(n): #j to numer kolumny. Przechodzi caly wiersz od lewej do prawej
            if i == j: #czyli przekatna bo numer wiersza = numer kolumny to przekatna
                row = row + [1] #to wtedy wartosci beda jako 1 
            else: 
                row = row + [0] #jesli nie jestesmy w glownej przekatnej to wartosci maja 0
        result = result + [row] #gotowy wiers dokladamy do macierzy
    return result

def print_matrix(m): #m to nasza macierz
    for row in m:
        for value in row:
            print(value, end=" ")
        print()

print_matrix(identity_matrix(5))
print()
print_matrix(identity_matrix(3))
print()
print_matrix(identity_matrix(8))
print()