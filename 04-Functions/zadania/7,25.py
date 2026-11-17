#Zdefiniuj funkcje, która zwraca sumę liczb z zakresu <x,y> całkowicie podzielnych przez 2 i 3, a niepodzielnych przez 4. 
def f(x,y):
    result = 0 #nasza suma liczb
    for i in range (x, y+1): #y+1 po to aby y tez sie wliczal w zakres. i to nasza liczba z zakresu
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            result = result + i #jesli warunek jest spelniony to dodajemy nasza liczbe do wyniku
    return result




x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("Result:",f(x,y))