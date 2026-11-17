#Zdefiniuj funkcję obliczającą x^n. Zastosuj rekurencję. Następnie oblicz 5^3. Zastosuj rekurencje
def power(x, n):
    if n == 0: #przypadek bazowy, kazda liczba do potegi 0 to jeden
        return 1
    return x * power(x, n-1) #x raxy x do potegi o jeden mniejszej

print(power(5,3))