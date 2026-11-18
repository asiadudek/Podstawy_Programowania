###
# Creates a shopping list based on product names
# entered from the keyboard.
#Napisz program, który pozwoli Ci utworzyć listę zakupów. 
#Program pobiera dane wejściowe użytkownika z klawiatury, aż użytkownik wprowadzi 0. 

# shopping list file name
shopping_list = 'shopping_list.txt' #nazwa plikow w ktorym zapisze sie lista zakupow

#adds product name at the end of a shopping list
#file_name - nazwa pliku, do którego zapisujemy
#product_name - nazwa produktu do zapisania (napis)
def add_product(file_name, product_name): #otwieramy plik w trybie dopisywania
   with open(file_name,'a') as file:
      file.write(product_name + '\n') #zapisujemy tekst do pliku i przechodzimy do nowej linii

# Takes next product name from the keyboard
product = "" #tutaj bedziemy umieszczac nasze wprowadzane produkty, narazie puste miejsce
while product != "0": #petla sie wykona dopoki produkt jest rozny od 0
   product = input('Enter product name (0 stops): ') #program prosi uzytkownika o wprowadzenie produktu
   if product == '0': #jesli produkt jest rowne 0
      break # stops entering food names ('while' breaks) - petla sie zatrzymuje
   else:
      add_product(shopping_list, product) #odwolanie do funkcji, jesli produkt jest rozny od zera to dopisujemy go do listy