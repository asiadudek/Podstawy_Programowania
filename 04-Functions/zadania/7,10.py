#program zwracajacy liczbę ujemnych liczb parzystych w zakresie<x,y>

def f(x,y):
    total = 0 #suma naszych ujemnych liczb parzystych

    for number in range(x,y+1): #petla przechodzi po kazdej liczbie z przedzialu. y+1 po to aby y wliczal sie do zakresu
        if number < 0 and number >= x and number <= y: #sprawdzamy czy liczba jest ujemna i miesci sie w zakresie x,y
            if number % 2 == 0: #teraz sprawdzamy czy dana liczba spelnia warunek parzystosci
                total = total + 1 #jesli spelnia oba powyzsze warunki to dodajemy ją do naszej sumy
    return total

    
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(f(x,y))