#Tablica zawiera liczby: -15, 8, -31, 47, -2, 19. Utwórz program, który znajdzie i wydrukuje maksymalną i minimalną liczbę.
arr = [-15, 8, -31, 47, -2, 19]

maximum = arr[0]
minimum = arr[0]

for x in arr:
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x

print("Array:",arr)
print("Maximum: ",maximum)
print("Minimum: ",minimum)
