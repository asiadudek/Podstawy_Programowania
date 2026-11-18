#Napisz program, który dla danej tablicy liczb rzeczywistych drukuje liczbę elementów większą od podanej wartości wprowadzonej z klawiatury.
numbers = [3.5, 7.2, 1.8, 9.4, 5.0, 6.1]

value = float(input("Enter value: ")) #wprowadzamy liczbe rzeczywista z klawiatury

counter = 0 #licznik elementow wiekszych od wprowadzonej wartosci
for x in numbers: #przeszukujemy elementy naszej tablicy
    if x > value: #jesli x jest wieksze od naszej wartosci z klawiatury
        counter += 1 #licznik zwieksza sie o 1

print("Number of elements greater than",value,":",counter)