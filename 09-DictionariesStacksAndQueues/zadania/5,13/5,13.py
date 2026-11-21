#Jeśli wprowadzona wartość jest liczbą, wciśnij liczbę na stos
#Jeśli wprowadzona wartość jest operatorem, wyjmij dwa elementy z górnej części stosu, wykonaj obliczenia i prześlij wynik operacji na stos.
#Jeśli wprowadzona wartość jest znakiem równości, wyjmij wynik końcowy ze stosu i wyświetl wynik obliczeń.


stack = [] #nasz pusty stos

while True: #petla dziala w nieskonczonosc az zatrzyma ja break
    value = input("Enter number, operator (+ - * /) or =: ")

    if value == '=':
        print("Result: ",stack.pop()) #to jest to koniec obliczen, zdejmujemy wynik ze stosu i wypisujemy
        break

    if value == '+' or value == '-' or value == '*' or value == '/':
        b = stack.pop() # ta liczba lezy na samym dnie stosu czyli byla dodana jako ostatnia czyli pierwsza wychodzi
        a = stack.pop() #zdejmujemy z wierzchu nastepna liczbe
        if value == '+':
            stack.append(a+b) #dodaje i odklada wynik na stos
        elif value == '-':
            stack.append(a-b)
        elif value == '*':
            stack.append(a*b)
        else:
            stack.append(a/b)
    else:
        stack.append(float(value))
