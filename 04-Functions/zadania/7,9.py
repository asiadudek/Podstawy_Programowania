#obliczającą sumę cyfr liczby. Gdy wartość parametru parzystego wynosi True, funkcja zwraca sumę cyfr parzystych. Gdy wartość parametru parzystego wynosi False, funkcja zwraca sumę cyfr nieparzystych. Przykładowy wynik:

def input_boolean(number, even):
    total = 0 #suma naszych cyfr parzystych lub nieparzystych

    for digit in number: #petla przechodzi po kazdej cyfrze 
        digit = int(digit) #zmieniamy cyfre jako ciag znakow na typ calkowity int
        if even == True: #jesli uzytkownik wybral sumowanie cyfr parzystych to zwracamy true
            if digit % 2 == 0:
                total = total + digit #jesli cyfra jest parzysta to dodajemy ją do naszej sumy
        else: #jesli uzytkownik nie wybral sumowania cyfr parzystych to sumujemy nieparzyste
            if digit % 2 != 0:
                total = total + digit #jesli cyfra jest nieparzysta to dodajemy ja do naszej sumy v2

    return total
    

number = input("Enter the number: ")
even = input("Summation of even digits? (True/False): ")
if even == "True":
    even = True
else:
    even = False

print("Summation:",input_boolean(number, even))
