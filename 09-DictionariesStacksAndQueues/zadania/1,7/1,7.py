#Napisz program, który drukuje:

#lista produktów i ilość
#całkowita liczba produktów w sklepie

products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}


for product, quantity in products.items():
    print(product, ":", quantity)

total = 0 #calkowita liczba produktow
for quantity in products.values():
    total = total + quantity
print("Total products:", total)

