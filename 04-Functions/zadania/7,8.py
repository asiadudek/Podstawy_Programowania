
# Program ktory zwraca minimalną liczbę monet, które można wykorzystać do zapłaty za zakupiony produkt

def how_many(amount_to_pay):
    coin_5 = 0 #licznik naszych monet, narazie jest ustawiony na 0
    coin_2 = 0
    coin_1 = 0
    while amount_to_pay >= 5:
        amount_to_pay = amount_to_pay - 5
        coin_5 = coin_5 + 1

    while amount_to_pay >=2:
        amount_to_pay = amount_to_pay - 2
        coin_2 = coin_2 + 1

    while amount_to_pay >=1:
        amount_to_pay = amount_to_pay - 1
        coin_1 = coin_1 + 1
        
    return coin_5 + coin_2 + coin_1

amount_to_pay = int(input("Enter amount to pay: "))
coin_5 = 0
coin_2 = 0
coin_1 = 0

print("Coins needed to pay:",how_many(amount_to_pay))