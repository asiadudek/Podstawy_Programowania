
def f(n):
    a = 0
    b = 1
    for i in range(n-1):#znamy juz pierwsza wartosc wiec musimy dac -1
        result = a + b
        a = b
        b = result
    return result

n = int(input("Enter n: "))
print(f(n))