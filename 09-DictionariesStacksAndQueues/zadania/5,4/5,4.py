#Słownik zawiera nazwy kursów i liczbę godzin. Napisz program, który oblicza i drukuje całkowitą liczbę godzin. 

winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}
total = 0 #calkowita liczba godzin
for value in winter_semester.values():
    total += value
    
print("The total number of hours in the winter semester is",total)