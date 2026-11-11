


price = float(input("Enter product's price: "))
discount = float(input("Enter the discount (%): "))
price_discount = price - (price * discount)/100 #cena po rabacie

print(f"Current price: {price_discount}")
print(f"Price before discount: {price}")

if discount >= 10:
    print("Buy a product!")
    print(f"Product's price has been reduced by {discount} %")
