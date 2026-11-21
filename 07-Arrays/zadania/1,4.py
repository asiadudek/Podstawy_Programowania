###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print("Number of elements: ",len(arr))
print("First value: ",arr[0])
print("Second value: ",arr[1])
print("Last value: ",arr[-1])
print("Last value: ",arr[4])
print("Summation of first and last value: ",arr[0]+arr[-1])
print("Median value ", arr[len(arr) // 2])


for i in arr: #"i" to kazdy element naszej tablicy, sprawdzamy go po kolei
    print(i, end=" ") #wypisujemy kazdy element w jednej linii

