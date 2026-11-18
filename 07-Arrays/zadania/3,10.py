#Dwie tablice zawierają następujące liczby całkowite [4,36,12,28,9,44,5] i [5,1,36]. 
#Utwórz program, który drukuje liczby z pierwszej tablicy, które nie pojawiają się w drugiej tablicy.
array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]

print("Array1:",array1)
print("Array2:",array2)
print("Numbers not in the second array:",end=" ")
for x in array1:
    if x not in array2:
        print(x, end=" ")