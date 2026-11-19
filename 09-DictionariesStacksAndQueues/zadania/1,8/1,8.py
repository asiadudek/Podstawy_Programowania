#Napisz program, który:

#drukuje listę produktów i ich ceny przed zniżką
#drukuje całkowitą wartość produktów przed rabatem
#modyfikuje cennik według rabatu (zaokrąglenie cen do dwóch miejsc po przecinku)
#drukuje listę produktów i ich ceny po 10% rabacie
#drukuje całkowitą wartość produktów po rabacie

price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for product, price in price_list.items():
    print(product, ":", price)

total_price = 0 #calkowita wartosc produktow przed rabatem
for price in price_list.values():
    total_price += price
print("Total products price: ", round(total_price,2))

for product, price in price_list.items():
    price_list[product] = round(price - (price * 0.1),2)
print(price_list)

total_price_discount = 0
for price in price_list.values():
    total_price_discount += price
print("Total price after discount: ", round(total_price_discount,2))