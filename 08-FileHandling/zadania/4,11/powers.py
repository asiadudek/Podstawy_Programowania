#Napisz program, który oblicza, drukuje i zapisuje w pliku tekstowym liczby całkowite od 1 do 100 oraz ich drugą i trzecią potęgę.

with open('powers.txt', 'w', encoding = 'UTF-8') as file: #tryb "w" tworzy plik od nowa, po kadym uruchomieniu jego wartosc jest nadpisywana
    for number in range(1, 101):
        sqaure = number ** 2
        cube = number ** 3
        line = (f"{number} {sqaure} {cube}")
        print(line) #wypisuje linie na ekranie
        file.write(line + '\n') #zapisuje linie do pliku i przechodzi do nowej linii
