#Tablica zawiera liczby całkowite: 2, 6, 4, 9, 7. Utwórz program, który drukuje wartości tablicy graficznie. 
#Zdefiniuj funkcje która zwraca podaną liczbę gwiazdek jako ciąg znaków.

numbers = [2, 6, 4, 9, 7]

def star(n):
    result = "" #puste miejsce gdzie bedziemy dodawac nasze gwiazdki
    for i in range(n): #powtarzamy petle n razy
        result += "*" #dodajemy gwiazdke do napisu
    return result

print("Numbers:",numbers)
for x in numbers: #przeszukujemy nasza tablice
    print(x,star(x)) #wyswietlamy numer z naszej tablicy a obok niego ilosc gwiazdek