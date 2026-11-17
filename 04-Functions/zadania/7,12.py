#Zdefiniuj funkcję f(n), która zwraca ciągn gwiazdek, oddzielonych znakiem ukośnika.

def f(n): #n to nasz argument czyli liczba gwiazdek
    total = "" #to tutaj beda przechowywane nasze gwiazdki
    
    for char in range(n): #petla powtorzy sie n razy
        if n > 1: #jesli n jest wieksze od 1
            total = total + "*" + "/"
        else:
            total = total + "*"
    return total

n = int(input("Enter number: "))
print(f(n))