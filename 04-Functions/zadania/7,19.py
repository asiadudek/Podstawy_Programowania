#Zdefiniuj funkcję zwracającą sumę powtarzających się cyfr w liczbie. 
def f(number):
    n = str(number) #przeksztalcamy liczbe na ciag znakow (string)
    total = 0 #poczatkowa wartosc cyfr powtarzajacych sie
    for i in n: #chodzimy po kazdej cyfrze naszej liczby
        if n.count(i) > 1:#jesli dana cyfra sie powtarza wiecej niz 1 raz
            total += int(i) #dodajemy to do sumy
    return total

number = int(input("Enter number: "))
print(f(number))