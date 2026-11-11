

hours = int(input("Enter the number of hours parked: ")) #podajemy liczbe godzin zaparkowania

if hours >= 1 and hours <= 2:
    print("You must pay 5 PLN")
elif hours >= 3 and hours <= 6:
    print("You must pay 15 PLN")
else:
    print("You must pay 20 PLN")