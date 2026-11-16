###
# Function that returns the full name of a day of the week
# based on its number
#

def day_name(day_number):
    if day_number == 1:
        day_name = "Monday"
    elif day_number == 2:
        day_name = "Tuesday"
    elif day_number == 3:
        day_name = "Wednesday"
    elif day_number == 4:
        day_name = "Thursday"
    elif day_number == 5:
        day_name = "Friday"
    elif day_number == 6:
        day_name = "Saturday"
    elif day_number == 7:
        day_name = "Sunday"
   
    return day_name

day_number = int(input("Enter day number: "))
print(f"The name of day {day_number} in the week is: {day_name(day_number)}")