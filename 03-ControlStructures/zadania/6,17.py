
time = input("Enter time (24h format): ") #pobieranie godziny od uzytkownika

hours = int(time[:2]) #pobieranie godziny czyli dwie pierwsze cyfry
minutes = time[3:5] #pobieranie minut czyli dwie ostatnie cyfry

if hours >= 12:
    period = "pm" #godzina po poludniu
else:
    period = 'am' #godzina przed poludniem

if hours > 12: 
    hours = hours - 12
elif hours == 0:
    hours = 12
print(f"Time in 12-hour format: {hours}:{minutes} {period}")
