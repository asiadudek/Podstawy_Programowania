###
# Credit card payment 
#

account_balance = 500 #ilosc srodkow na koncie
total_payment = float(input("Enter your total payment: ")) #calkowita kwota do zaplaty
if total_payment <= account_balance: 
    print(f"Payment completed")
else:
    print(f"No funds") #brak srodkow na koncie