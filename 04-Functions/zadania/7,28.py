#Sekwencja cyfr zawiera liczbę punktów rzuconych kostką. 
#Zdefiniuj funkcje zwracającą liczbę określającą liczbę rzuconych kości najczęściej z rzędu.

def f(dice):
    for length in range(len(dice), 0 ,-1):#czyli idziemy od końca do początku, sprawdzamy najdluzsza serie jednej cyfry
        for digit in "123456": #sprawdzamy po kolei kazda cyfre
            if digit * length in dice: #to  nie mnozenie tylko powielanie np 3*2 to 33 albo 5*6 to 555555 bo mamy typ str
                return int(digit) #pierwsza znaleziona seria jest najdluzsza wiec zwracamy te cyfre jako liczbe

dice = input("Enter dice: ")
print(f(dice))


