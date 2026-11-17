#Produkty oznaczone są specjalnym kodem składającym się z 3 cyfr i czwartej cyfry kontrolnej.
#Czwartą cyfrę ustala się, obliczając pozostałą część po podzieleniu sumy pierwszych trzech cyfr przez 7
#Zdefiniuj funkcje, która zwraca informację True, czy kod produktu jest poprawny, czy False

def f(product_code):
    result = 0 #suma trzech pierwszych cyfr, na poczatku wynosi 0
    for i in range(3): #i przyjmuje pozycje od 0 do 2 czyli pierwsze trzy cyfry
        result = result + int(product_code[i]) #bierzemy cyfre z pozycji i, i dodajemy ją do naszej sumy
    rest = result % 7 #obliczamy reszte z dzielenia sumy naszych trzech pierwszych cyfr
    return rest == int(product_code[3]) #porownujemy nasza reszte z czwarta cyfra kodu wprowadzona przez uzytkownika. Jesli sie zgadza to zwracamy True


product_code = input("Enter product code: ")
print(f(product_code))