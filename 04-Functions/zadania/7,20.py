#Zdefiniuj funkcje zwracającą n-tą liczbę pierwszą

def f(n):
    found = 0 # ile liczb pierwszych już znalazłam
    number = 1 # liczba, którą aktualnie sprawdzam

    while found < n: #powtarzamy dopoki nie znajdziemy tylu liczb pierwszych ile wynosi nasza liczba wprowadzona z klawiatury
        number = number + 1 #przechodzimy do nastepnej liczby ktora chce sprawdzic
        is_prime = True #zakladamy, ze to liczba pierwsza dopoki nie znajdziemy dwoch dzielnikow

        for d in range(2, number): #petla powtorzy sie od 2 do number -1. Sprawdzamy wszystkie dzielniki od 2 do naszej liczby pomniejszonej o jeden
            if number % d == 0: #jesli liczba dzieli sie bez reszty
                is_prime = False #to nie jest liczba pierwsza
                break #petla sie zatrzymuje bo dalsze sprawdzanie nie ma sensu
        if is_prime: #jesli liczba jest pierwsza bo nie dzieli sie na liczby od 2 do naszej liczby pomniejszonej o 1
            found = found + 1 #dodajemy ja do naszego licznika
    return number


n = int(input("Enter n: "))
print("Prime numbers:",f(n))