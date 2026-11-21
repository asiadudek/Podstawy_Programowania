#Napisz program, który pobiera dane z klawiatury o zakupionym produkcie:
#nazwa
#cena (liczba rzeczywista z dwoma miejscami po przecinku)
#zapłacono (tak/nie)
#Następnie program zapisuje dane produktu w pliku product.json.

import json 

product = {} #pusty slownik; za chwilę dodamy do niego trzy informacje o produkcie

product['name'] = input("Product name: ")
product['price'] = float(input("Product price: "))

paid = input("Paid (yes/no): ")

if paid == "yes":
    product['paid'] = True
else:
    product['paid'] = False


with open('products.json', 'w', encoding = 'UTF-8') as file:
    json.dump(product, file, indent=4)