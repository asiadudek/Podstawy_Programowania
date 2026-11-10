###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time #importujemy modul time, ktory pozwala na wstrzymanie wykonywania programu na okreslony czas

countdown = int(input("Enter the number of seconds to count down: ")) #uzytkownik wprowadza liczbe sekund odliczania

while countdown > 0: #petla wykonuje sie dopoki countdown czyli liczba sekund jest wieksza od 0
    if countdown == 5:
        print("Five")
    elif countdown == 4:
        print("Four")
    elif countdown == 3:
        print("Three")
    elif countdown == 2:
        print("Two")
    elif countdown == 1:
        print("One")
    else: #jesli countdown czyli liczba sekund jest wieksza od 5 to wyswietlamy sekundy w postaci liczby
        print(countdown) 
    countdown -= 1
    time.sleep(1)  # Wait for 1 second  #time.sleep(1) wstrzymuje program na 1 sekunde przez co widzimy odliczanie w czasie rzeczywistym

print("Time's up!")