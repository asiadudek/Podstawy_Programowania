
circumference = int(input("Enter tree circumference: ")) #podajemy obwod pnia
diameter =  circumference / 3.14159  #obliczamy srednice drzewa obwod/liczbe pi
can_cut = diameter >= 50  #to zwraca wartosc bool
print(f"Tree can be cut down: {can_cut}")              