#Napisz program, który obliczy całkowity koszt koszyka za pomocą cennika.


# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
total = 0 #calkowity koszt, narazie wynosi 0
for product, quantity in cart.items():
    total += prices[product] * quantity

print("Total cost: ", round(total, 2))
