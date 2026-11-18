

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

# Bubble sort
#
def bubble_sort(arr):
    n = len(arr) #ilosc elementow listy
    for i in range(n):#numer rundy, petla wykona sie tyle razy ile tablica zawiera elementow. i mowi ktory raz petla sie wykonuje
      for j in range(n-i-1): #pozycja sasiadujacych liczb, na ktorym miejscu jestesmy
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)