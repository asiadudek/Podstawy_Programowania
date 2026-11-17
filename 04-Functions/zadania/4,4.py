###
# Calculates the sum of the digits in a number
#Suma cyfr w danej liczbie

def sum_digits(number): #nasza funkcja
    number = abs(number) #abs zamienia nam liczbe ujemna na dodatnia (wartosc bezwzgledna)
    text = str(number) #str zamienia nam nasza liczbe na ciag znakow czyli na tekst. Po liczbie nie da sie przeprowadzic petli musi byc str
    total = 0 #nasza poczatkowa suma cyfr w naszej liczbie. narazie wynosi 0

    for digit in text: #sprawdzamy kazdy znak czyli cyfre w liczbie
        total += int(digit) #do naszej sumy poczatowej dodajemy kazda cyfre tworząca liczbe
    return total

number = int(input("Enter a number: ")) 
print(f"The sum of digits is: {sum_digits(number)}")

