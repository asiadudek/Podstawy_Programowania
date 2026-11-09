###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int(input("Enter car speed (km/h): "))
if car_speed > 140:
    print(f"Your speed is: {car_speed} km/h")
    print(f"Warning: Speed limit exceeded!") #predkosc zostala przekroczona
else:
    print(f"Your speed is: {car_speed} km/h")