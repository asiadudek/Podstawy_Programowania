###
# Sums numbers entered by user
#

total_sum = 0 #zmienna przechowujaca sume wprowadzonych liczb

while True: #petla wykonuje sie dopoki jest prawdziwa 
    number = int(input("Enter a number (0 to stop): ")) #liczba wprowadzona przez uzytkownika, konwertowana na int

    if number == 0: #jesli uzytkownik wprowadzi 0 to przerywamy petle
        break 
    total_sum += number #suma wprowadzonych liczb

print (f"The total sum of the numbers is: {total_sum}")