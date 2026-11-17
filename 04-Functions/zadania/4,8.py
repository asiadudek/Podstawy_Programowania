

def time_string(hours, minutes, time_format): #funkcja przybiera 3 argumenty
    if time_format == "12":
        hours = hours % 12 #reszta z dzielenia
        if hours == 0:
            hours = 12

    if minutes < 10:
        minutes_text = "0" + str(minutes)
    else:
        minutes_text = str(minutes)

    return (f"{hours}:{minutes_text}")

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
time_format = input("Enter time format: ")

print(time_string(hours, minutes, time_format))
