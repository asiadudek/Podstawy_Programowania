###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = speed_kmh / 3.6 #1km - 1000m, 1h = 60min x 60 sek = 3600 sek, 1kmh = 1000m/3600s = 1/3.6 m/s
print(speed_kmh, "km/h", "=", round(speed_ms,2), "m/s")