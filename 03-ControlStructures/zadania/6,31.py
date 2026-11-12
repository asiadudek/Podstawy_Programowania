#Program wyswietla nam 20 losowych liczb w zakresie od 5 do 10
import random

for i in range(20):
    liczba = random.randint(5,10)
    print(liczba, end=" ")
