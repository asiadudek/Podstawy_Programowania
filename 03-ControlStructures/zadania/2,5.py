###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input("Enter month number: "))

if month <= 3 and month != 0:
    quarter = 1 #kwartal
elif month > 3 and month <= 6:
    quarter = 2
elif month > 6 and month <= 9:
    quarter = 3
elif month > 9 and month <= 12:
    quarter = 4
else:
    print("Invalid month number.")
    print(f"Month {month} does not exist.")

if month > 0 and month <= 12:
    print(f"Month {month} is in quarter {quarter}.")