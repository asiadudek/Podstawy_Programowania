class BankAccount:
    def __init__(self, number):
        self.account_number = number #zapisujemy numer konta w obiekcie
        self.balance = 0 #saldo na start wynosi 0

    def deposit(self, amount):
        self.balance  += amount #wplata zwieksza nasze srodki na koncie

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("No funds")

    def show_balance(self):
        print(f"Bank Account number: {self.account_number}")
        print(f"Balance: {self.balance:.2f}")
