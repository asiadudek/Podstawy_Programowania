#ciag fibonacciego
a = 0 #pierwszy znak
b = 1 #drugi znak
for i in range(20): #petla wykona sie 20 razy
    print(a, end=" ") #a wyswietla sie w jednej linii
    #liczymy znaki w ciagu fibonacciego. Kolejny wyraz jest sumą dwóch poprzednich liczb
    suma = a+b #obliczamy sumę
    a=b #czyli a staje sie b
    b = suma #b staje sie sumą
