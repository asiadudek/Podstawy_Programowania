###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#

driving_mode = input("Enter driving_mode (A/M/E) ") #podajemy tryb jazdy
distance = int(input("Enter distance in km: ")) #podajemy dystans

if driving_mode == "A":
    fuel_consumption = 7 #zuzycie paliwa na 100km
elif driving_mode == "M":
    fuel_consumption = 9
else:
    fuel_consumption = 6

total_consumption = distance * fuel_consumption /100 #calkowite zuzycie paliwa
print(f"Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters.")