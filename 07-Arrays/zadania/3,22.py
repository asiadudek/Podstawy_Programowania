#Zdefiniuj funkcję rand_elem(array), która zwraca losowo wybrany element tablicy. 
import random

def rand_elem(array):
    index = random.randint(0,len(array) - 1) #index to pozycja elementu w tablicy, funkcja ta losuje numer z poczatkiem i koncem wlacznie!
    return array[index]

numbers = [10, 20, 30, 40, 50, 60]

print("Array", numbers)

for i in range(5): #i to licznik powtorzen, to nie jest index
    print("Random element: ", rand_elem(numbers))