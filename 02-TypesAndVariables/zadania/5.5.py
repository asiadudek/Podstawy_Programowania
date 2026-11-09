
price = float(input("Enter the price: "))
discount = float(input("Enter the discount: "))
reduction = (price * discount) / 100 #ile zl wynosi znizka
price_with_discount = price - reduction
print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {reduction:.2f}")