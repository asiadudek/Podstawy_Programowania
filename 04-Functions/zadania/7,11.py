#Zdefiniuj funkcję,f(n1,n2,n3) która zwraca wartość True, jeśli przynajmniej jedna z liczbn1,n2,n3 jest ujemna lub fałszywa, w przeciwnym wypadku False

def input_boolean(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0: #jesli przynajmniej jedna z liczb jest ujemna to zwracamy wartosc True
        return True
    else:
        return False #jesli wszystkie liczby są dodatnie to zwracamy wartosc False

n1 = int(input("Enter a number n1: "))
n2 = int(input("Enter a number n2: "))
n3 = int(input("Enter a number n3: "))
print(input_boolean(n1,n2,n3))