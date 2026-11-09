###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = int(input("Enter number: ")) #prosimy o podanie liczby

if number % 2 == 0: #dzielenie z resztą
    print(f"{number} is even") #komunikat, że liczba jest parzysta
else:
    print(f"{number} is odd.") #pokazuje nam komunikat, że liczba jest nieparzysta