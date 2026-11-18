###
# Prints vehicle registration numbers from Krakow
#Napisz program, który drukuje numery rejestracyjne samochodów z Krakowa. Numeruj wydrukowaną listę.
polish_license_plates = [
   'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
   'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
   'KK54985', 'LU4864U'
]
counter = 1 #licznik pozycji
for car_number in polish_license_plates:
   if car_number[0:2] == "KR" or car_number[0:2] == "KK":
      print(counter, car_number)
      counter += 1 #po kazdym wypisaniu danej wartosci zwiekszamy numer wiersza w nowej linijce