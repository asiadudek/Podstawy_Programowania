
def second_largest(array): #zwraca drugi co do wielkosci element
    first = None #pierwszy element najwiekszy, narazie nic nie mamy
    second = None #drugi element najwiekszy, narazie nic nie mamy
    for x in array: #przeszukujemy wszystkie liczby w naszej tablicy
        if first is None or x > first: #sprawdzamy warunek, jesli first jest puste lub x jest wieksze od first
            second = first #stara liczba ktora najwieksza staje sie teraz druga najwieksza liczba
            first = x #x jest teraz najwieksza liczba
        elif x != first and (second is None or x > second): #jesli x jest rozne od first i second jest puste lub x jest wieksze od second
            second = x #x staje sie druga najwieksza liczba
    return second

def smallest_and_largest(array): #funkcja zawierajaca tablice [najmniejsza, najwieksza]
    smallest = array[0] #na start najmniejsza to pierwszy element
    largest = array[0] #na start najwieksza to pierwszy element
    for x in array: #przeglądamy wszystkie wartosci w tablicy
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    return [smallest, largest] #zwracamy dwuelementowa tablice

def difference(array): #zwraca roznice miedzy najwieksza a najmniejsza wartoscia
    result = smallest_and_largest #korzystamy z funkcji smallest_largest
    return result[1] - result[0]


def median(array): #zwraca wartosc srodkowa
    arr = array[:] #robimy kopie listy zeby nie zmienic oryginalu
    n = len(arr) #n to liczba elementow naszej tablicy
    for i in range(n - 1): #tyle razy nasza petla ma sie wykonac
        for j in range(n - 1 - i): #sprawdzamy pary liczb, odejmujemy i jesli nasza liczba zostala juz sprawdzona i zmienila miejsce
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    middle = n // 2 #srodkowa pozycja
    if n % 2 == 1: #jesli mamy nieparzysta liczbe elementow
        return arr[middle]
    return (arr[middle - 1] + arr[middle]) / 2 #gdy mamy parzysta liczbe elementow to wtedy mediana to srednia arytm dwoch srodkowych liczb

def to_string(array): #zwracamy elementy tablicy jako ciag znakow oddzielonych -
    result = "" #miejsce gdzie wlozymy nasz ciag znakow
    for i in range(len(array)): #i to numer pozycji, len(array) to liczba elementow
        if i > 0: #jesli numer pozycji jest wiekszy od 0
            result += "-" #najpierw do naszego miejsca doklejamy -
        result += str(array[i]) #nastepnie doklejamy nasza liczbe zamieniona na typ str
    return result