from bank import BankAccount

def main():
    account = BankAccount("12 3456 5555 9090 1111 0000 7722") #nasz obiekt czyli numer konta
    
    account.show_balance()
    account.deposit(25.30)
    account.show_balance()
    account.withdraw(31.70)
    account.show_balance()
    account.withdraw(14)
    account.show_balance()

if __name__ == "__main__":
    main()