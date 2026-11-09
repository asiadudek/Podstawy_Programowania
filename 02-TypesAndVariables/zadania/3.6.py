#Odległość do horyzontu z wysokosci mojego wzrostu
import math
height = float(input("Enter the height in meters: "))
distance = 3.57 * math.sqrt(height)
print("The distance is:",round(distance,2))

#Odleglosc do horyzontu z wysokosci okna w hotelu (20meters)
height_2 = 20
distance = 3.57 * math.sqrt(height_2)
print("The distance is:", round(distance,2))