###
# Checks if the given day number of the month is correct
#

month = int(input("Enter month number (1-12): "))
day = int(input("Enter day number: "))
day_ok = False #Nie wiemy czy dzien jest poprawny, wiec zakładamy, ze nie jest

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day >= 1 and day <=31:
        day_ok = True
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day <=30:
        day_ok = True
else:
    if day >=1 and day <= 28:
        day_ok = True

message = (f'Day {day} for the month {month}')
if day_ok: #warunek, jesli dzien jest poprawny to wyswietlamy komunikat, ze jest poprawny
    print(f"{message} is correct")
else: #jesli dzien nie jest poprawny to wyswietlamy komunikat, ze jest niepoprawny. Else oznacza w przeciwnym razie
    print(f"{message} is incorrect")
