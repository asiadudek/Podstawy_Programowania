###
# A simple number guessing game
#


import random
# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100) #zmienna przechowujaca losowa liczbe z przedzialu od 1 do 100
user_guess = 0 #zmienna przechowujaca liczbe podana przez uzytkownika, narazie wynosi 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess: #petla wykonuje sie dopoki liczba podana przez uzytkownika jest rozna od liczby wylosowanej przez komputer
    user_guess = int(input("Enter your number: ")) #uzytkownik podaje liczbe, ktora jest przypisywana do zmiennej user_guess

    if user_guess < number_to_guess: #warunek sprawdzajacy czy liczba podana przez uzytkownika jest mniejsza od liczby wylosowanej przez komputer
        print("Too low! Try again")
    elif user_guess > number_to_guess:
        print("Too high! Try again")
    else: 
        print("Congratulations! You guessed the correct number!")
