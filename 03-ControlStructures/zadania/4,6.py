###
# Calculates the sum of integer numbers in the range <1,5>
#

sum = 0 #zmienna przechowujaca nasza sume, narazie wynosi 0
for a in range (5,11): #petla for przeszukuje liczby od 5 do 10. "a" oznacza nasze liczby w tym przedziale
    sum += a #dodajemy do sumy kolejne liczby z przedzialu

print(f"Sum is {sum}")