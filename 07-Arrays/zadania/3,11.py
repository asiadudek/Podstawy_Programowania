#Utwórz program sortujący elementy tablicy zawierającej liczby całkowite. Zastosuj algorytm sortowania Bubble Sort
arr = [[64, 34, 25, 12, 22, 11, 90], [5, -3, 0, 8, -10, 7],
[3, 3, 1, 2, 1],
]
def bubblesort(array):
    n = len(array) #ilosc elementow
    for i in range(n):
        for j in range(n-i-1): #w nawiasie mamy liczbe par, ktora musimy jeszcze porownac, -1 apobiega wyjsciu poza liste
            if array[j] > array[j+1]: #i to najwieksza z posortowanych liczb, odejmujemy zeby jej nie sprawdzac znowu
                array[j], array[j+1] = array[j+1], array[j]
    return array

for x in arr:
    print("Array: ",x)
    print("Sorted Array:",bubblesort(x))
    print()
