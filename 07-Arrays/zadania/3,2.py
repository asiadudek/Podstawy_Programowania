#Tablica zawiera liczby naturalne: 15, 8, 31, 47, 2, 19. Utwórz program, który drukuje zawartość tablicy w odwrotnej kolejności
arr = [15, 8, 31, 47, 2, 19]

for value in arr[::-1]:
    print(value, end=" ")

