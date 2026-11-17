#Zdefiniuj funkcje która dla danej liczby naturalnej n oblicza sumę wszystkich liczb naturalnych pomiędzy 1 a n. 
#zastosuj rekurencje
def sum_natural(n):
    if n == 1: #przypadek bazowy, dla kazdego n rownego 1 suma wynosi tez 1
        return 1
    return n + sum_natural(n-1) #nasza liczbe ktora wprowadzilismy wyciagamy przed nawias, a w nawiasie sumujemy liczby od niej mniejsze

print(sum_natural(10))
    