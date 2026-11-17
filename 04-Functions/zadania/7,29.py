def factorial(n): 
    # 0! = 1, 1! = 1
    if n == 0 or n == 1: #jesli n = 0  lub 1
        return 1 #zwracana wartosc jest jeden
    # n! = n * (n-1)!
    return n * factorial(n - 1) 


print(factorial(5))