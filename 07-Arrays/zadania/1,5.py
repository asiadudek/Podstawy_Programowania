
arr = [1, 2, 3, 4, 5]
print(arr)

arr[0] = arr[0] - 1 #zmiana wartosci pierwszego elementu
print(arr)

arr[-1] = arr[-1] + 4 #zmiana wartosci drugiego elementu
print(arr)

arr[len(arr) // 2] = arr[len(arr) // 2]* 2
print(arr)