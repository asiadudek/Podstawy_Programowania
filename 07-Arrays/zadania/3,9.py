#Zdefiniuj funkcje która zwraca wartość True, jeśli obie tablice są takie same, lub False w przeciwnym wypadku. 
#Dwie tablice są takie same, jeśli mają taką samą liczbę elementów, a wartości elementów w komórkach tablic o tym samym indeksie są równe
def compare(array1, array2):
    if len(array1) != len(array2): #najpierw porownujemy dlugosci tablic
        return False #jesli jest rozna ilosc elementow to konczymy od razu i zwracana jest wartosc False
    for i in range(len(array1)): #i to numer pozycji, len(array1) ilosc elementow tablicy 1. Do sprawdzenia wystarczy nam jedna jesli obie maja takie same dlugosci
            if array1[i] != array2[i]: #jesli wartosc na pozycji w tablicy 1 i 2 są rozne to tablice nie sa takie same
                return False
    return True #zwraca funkcja wartosc true jesli tablice sa takie same

#para 1
a1 = ["water","book","sky"]   
a2 = ["water","book","sky"]
print("Array1",a1)
print("Array2",a2)

if compare(a1,a2):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are different")
print()



#para 2
a1 = [True,False]  
a2 = [True,False,True]
print("Array1",a1)
print("Array2",a2)

if compare(a1,a2):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are different")
print()

#para3
a1 = [5,3,1] 
a2 = [5,3,1]
print("Array1",a1)
print("Array2",a2)

if compare(a1,a2):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are different")
print()

#para4
a1 = [3,2,1]   
a2 = [3,2]
print("Array1",a1)
print("Array2",a2)

if compare(a1,a2):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are different")
print()
