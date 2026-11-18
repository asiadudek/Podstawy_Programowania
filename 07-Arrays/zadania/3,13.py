#Zdefiniuj funkcję occurs(number, array), która zwraca wartość True, jeśli dana liczba znajduje się w tablicy. 
#Następnie utwórz program, który sprawdza, czy liczba wprowadzona z klawiatury znajduje się w tablicy [15, 38, 7, 23, 14]. 

def occurs(number,array):
    for x in array:
        if x == number:
            return True
    return False


array = [15, 38, 7, 23, 14]
number = int(input("Enter number: "))

print("Array: ",array) #wypisujemy nasza tablice

if occurs(number, array): #jesli True
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appears in the array")
