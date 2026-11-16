

def time_string(hours, minutes, time_format):
    if time_format == "12":
        hours = hours % 12
        if hours == 0:
            hours = 12
    elif time_format == "24":
        hours = hours

    return (f"{hours}:{minutes:.2f}")

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
time_format = input("Enter time format: ")

print(time_string(hours, minutes, time_format))
