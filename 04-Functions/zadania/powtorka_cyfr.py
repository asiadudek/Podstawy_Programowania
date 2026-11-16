
def f(number):
    s = str(number) #przeksztalcamy liczbe na ciag znakow (string)
    total = 0 #poczatkowa wartosc cyfr powtarzajacych sie
    for i in s: #ile cyfr miesci sie w naszej stringowej liczbie
        if s.count(i) > 1:#jesli dana cyfra sie powtarza wiecej niz 1 raz
            total += int(i)#dodajemy to do sumy

    return total

number = int(input("Enter number: "))
print(f(number))