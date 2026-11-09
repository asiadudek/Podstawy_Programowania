###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#

distance = int(input("Enter distance in km: "))
fuel_price = float(input("Enter fuel price per liter: "))
fuel_consumption = float(input("Enter fuel consumption per 100 km: ")) #wpisujemy ile litrów paliwa zużywamy na 100km
total_fuel_consumption = distance * fuel_consumption / 100 #dzielimy na 100 bo zuzycie mamy na 100km
total_cost = fuel_price * total_fuel_consumption
print(f"Total fuel consumption: {total_fuel_consumption:.2f} liters.")
print(f"Total cost: {total_cost:.2f}")