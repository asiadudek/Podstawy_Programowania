
amount = int(input("Enter amount: "))
coin_1 = 0
coin_2 = 0
coin_5 = 0

while amount >= 5: #petla wykouje sie dopoki warunek jest spelniony, sprawdza czy kwota jest wieksza od 5
    amount = amount - 5 #jesli warunek jest spelniony to odejmujemy 5 od kwoty
    coin_5 = coin_5 + 1 #zwiekszamy licznik monet o 1. Sprawdzamy ile razy w naszej kwocie miesci sie 5zl

while amount >= 2:
    amount = amount - 2
    coin_2 = coin_2 + 1

while amount >= 1:
    amount = amount - 1
    coin_1 = coin_1 + 1

print(f"Coin 5: {coin_5}")
print(f"Coin 2: {coin_2}")
print(f"Coin 1: {coin_1}")