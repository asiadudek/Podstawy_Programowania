#Poniższe dane przedstawiają układ miejsc siedzących w kinie. Napisz program, który:

#oblicza, ile miejsc jest dostępnych
#oblicza, ile miejsc jest zarezerwowanych
#informuje, jaki jest status miejsca w danym rzędzie i danym miejscu (dostępnym lub zarezerwowanym)

# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   count = 0 #licznik ilosci siedzen, narazie wynosi 0
   for row in seats: #przeszukujemy kazdy rzad w tablicy
      for seat in row: #przeszukujemy kazde siedzenie w rzedzie
        count += 1 #kazde miejsce zwieksza licznik o 1
   return count
         

def seats_available(seats): #zwraca miejsce dostepne
   count = 0 #licznik miejsc dostepnych, narazie wynosi 0
   for row in seats: #przeszukujemy rzad w tablicy
      for seat in row: #przeszukujemy kazde miejsce w rzedzie
         if seat == "A": #jesli siedzenie to A czyli dostepne
            count += 1 #to zwiekszamy wtedy licznik dostepnych miejsc
   return count

def seats_booked(seats): #zwraca miejsca zajete
   count = 0 #licznik miejsc zajetych, narazie wynosi 0
   for row in seats: #przeszukujemy kazdy rzad w tablicy
      for seat in row: #przeszkujemy kazde miejsce w rzedzie
         if seat == "B": #jesli siedzenie to B czyli zajete
            count += 1 #to zwiekszamy wtedy licznik zajetych miejsc
   return count

def seat_status(seats, row, place): #sprawdza status danego miejsca
   seat = seats[row - 1][place - 1] #odejmujemy 1 bo python zaczyna indeksowac od 0 a nie od 1
   if seat == "A":
      return "available"
   else:
      return "booked"
      


print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:',seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))