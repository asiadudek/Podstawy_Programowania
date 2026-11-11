

products = int(input("Enter number of products purchased: ")) #uzytkownik wprowadza ilosc kupionych produktow
price = int(input("Enter price of one product: "))

if products <= 2: #jesli kupiono 2 lub mniej produktow to cena jest liczona normalnie
    total = products * price
else: #jesli kupiono wiecej niz 2 produkty to cena za 2 produkty jest liczona normalnie a za pozostale produkty cena jest liczona z 25% obnizka
    total = 2 * price + (products - 2) * price * 0.75 

print(f"Amount to pay: {total:.2f}")