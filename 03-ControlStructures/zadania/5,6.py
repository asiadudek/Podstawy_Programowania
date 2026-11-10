###
# Calculates the sum of even numbers from 1 to a given number N
#

N = 10
sum_even = 0

i = 1 #nasza liczba poczatkowa
while i <= N: #petla wykonuje sie dopoki liczba czyli 'i' jest mniejsza lub rowna N
    if i % 2 == 0: #jesli liczba jest parzysta to dodajemy ja do sumy
        sum_even += i
    i += 1 #przechodzimy do kolejnej liczby, dlatego zwiekszamy liczbe o 1, przesuwamy sie w prawo

print(f"Total sum even numbers: {sum_even}")