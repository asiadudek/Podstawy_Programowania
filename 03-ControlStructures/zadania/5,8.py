###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True: #petla nieskonczona, trwa do momentu az uzytkownik nie wybierze opcji wyjscia
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: ")) #uzytkownik wprowadza kwote do wplaty na konto
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: ")) #uzytkownik wprowadza kwote do wyplacenia z konta
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.") #informacja dla uzytkownika, ze nie ma wystarczajacych srodkow do wyplaty na koncie
    elif choice == '4':
        print(f"Your PIN is: {pin}")
    elif choice == '5':
        new_pin = input("Enter new PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit(): #sprawdzamy czy nowy pin ma 4 cyfry i czy sklada sie tylko z cyfr
            pin = new_pin #jesli warunek jest spelniony to zmieniamy pin na nowy
            print("Your PIN has been changed")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")