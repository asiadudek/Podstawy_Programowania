#Zdefiniuj funkcję f(n), która zwraca n-tą wartość ciągu Fibonacciego. 
#Sekwencję definiuje się następująco: pierwsza wartość sekwencji wynosi 0, druga wartość wynosi 1. 
#Każda kolejna wartość jest sumą dwóch poprzednich.

def f(n):
    a = 0
    b = 1
    for i in range(n-1): #bo znamy juz pierwszy wyraz ciagu, jest nim a, dlatego -1
        result = a + b #nasza liczba w ciagu fibonacciego
        a = b #a przyjmuje wartosc b
        b = result #b przyjmuje wartosc sumy
    return a #tutaj stoimy n n-tym wyrazie z ciagu fibonacciego

n = int(input("Enter n: "))
print(f(n))