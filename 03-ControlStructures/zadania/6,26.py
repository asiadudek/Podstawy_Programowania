


correct = False #zmienna przechowuje informacje o tym czy pin jest poprawny

for i in range(3): #petla wykona sie 3 razy, uzytkownik ma 3 proby na wpisanie poprawnego pinu
    pin = input("Enter your pin (4numbers): ") #prosba o podaniie pinu (pojawi sie do 3 razy)
    if pin == "0734":
        correct = True
        break #poprawny pin wiec wychodzimy z petli od razu

if correct: #jesli correct jest True to wyswietlamy komunikat o poprawnym pinie
    print("Your pin is correct")
else:
    print("Your pin is incorrect")
    print("Sorry your card has been blocked.")
    
