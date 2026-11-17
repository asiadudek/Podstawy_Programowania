#Wyrażenie zawiera operatory dodawania i odejmowania liczb jednocyfrowych. Zdefiniuj funkcje zwracającą wartość wyrażenia
def f(expression):
    result = 0 #wynik, narazie wynosi 0
    operator = "+" #zakladamy ze operator to +
    for char in expression: #przeszukujemy znaki w naszym dzialaniu
        if char == "+" or char == "-": #jesli znak jest + lub -
            operator = char #to znak jest opratorem
        else:
            digit = int(char) #zamieniamy nasz znak, cyfre na liczbe calkowita abysmy mogli robic operacje
            if operator == "+": 
                result = result + digit
            else:
                result = result - digit
    return result


expression = input("Enter expression: ") #wprowadzamy nasze dzialanie
print("Result:",f(expression))