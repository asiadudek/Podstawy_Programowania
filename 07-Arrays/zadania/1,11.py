###
# The weather station report
#Napisz program, który analizuje temperaturę na podstawie obserwacji z marca i drukuje następujący raport
temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# number of mesaurements
mesaurements = len(temperatures) #liczba pomiarow

# calculates average temperature
temp_total = 0 #suma wszystkich temperatur
for temp in temperatures:
   temp_total += temp
avg_temp = temp_total / len(temperatures)

# calculates min and max temperatures
min_temp = min(temperatures)
max_temp = max(temperatures)

# calculates number of days with negative temp
negative_temp = 0 #licznik dni z ujemna temperatura
i = 0 #pozycja temperatury
while i < len(temperatures): #petla sie wykona dopoki pozycja danego elemenu jest mniejsza od liczby pomiarow
   if temperatures[i] < 0:
      negative_temp += 1 #to zwiekszamy nasz licznik o 1
   i += 1

# prints out month report
print("TEMPERATURE REPORT")
print("Month: March")
print("Number of mesaurements:",mesaurements)
print("Average temperature in the month:",avg_temp)
print("Minimum temperature:",min_temp)
print("Maximum temperature:",max_temp)
print("Number of days with negative temperature:",negative_temp)