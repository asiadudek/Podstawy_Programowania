#Zdefiniuj funkcjęf(n), która zwraca liczby od 1 do n jako ciąg znaków

def f(n):
    result = "" #zmienna ktora przechowuje nasz ciag znakow, narazie jest pusta
    for i in range(1,n+1): #n+1 aby nasz liczba ktora podamy czyli n tez byla w zakresie. Petla wykona sie od 1 do naszej liczby n
        result += str(i) #ciag znakow wiec musimy tu zrobic string
    return result

n = int(input("Enter n: "))
print(f(n), end="")