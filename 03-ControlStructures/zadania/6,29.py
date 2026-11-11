

n = int(input("How many prime numbers to print? ")) #ile liczb pierwszych wypisac

found = 0 #licznik ile liczb pierwszych znaleziono
number = 2 #liczba ktora aktualnie sprawdzamy. Zaczynamy od 2 bo 2 to najmniejsza liczba pierwsza

print("Prime numbers: ", end=" ")

while found < n: #petla wykonuje sie dopoki znaleziono mniej niz liczba szukanych liczb pierwszych
    divisors = 0 # liczba dzielnikow. Na poczatku sprawdzania kazdej liczby on sie zeruje
    for d in range(1, number + 1): #petla zawierajaca cyfry przez ktore probujemy dzielic nasze liczby.
        if number % d == 0: #jesli liczba dzieli sie bez reszty przez d to znaczy ze d jest jej dzielnikiem
            divisors = divisors + 1 #zwiekszamy licznik dzielnikow o 1
    if divisors == 2: #jesli liczba dzielnikow wynosi 2 to znaczy, ze liczba jest pierwsza bo liczba pierwsza dzieli sie przez 1 i przez sama siebie
        print(number, end=" ") #wypisujemy liczbe pierwsza
        found = found + 1 #zwiekszamy licznik znalezionych liczb pierwszych o 1
    number = number + 1 #zwiekszamy liczbe ktora sprawdzamy o 1 bo chcemy sprawdzic kolejna liczbe

