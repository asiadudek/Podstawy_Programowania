#Program, który oblicza wynagrodzenie pracownika, biorąc pod uwagę możliwość otrzymania premii. 
#Następnie oblicza całkowite wynagrodzenie pracownika dla następujących przypadków
#Pracownik nie otrzymuje premii#
#Pracownik otrzymuje premię w wysokości 30%
##

basic_salary = 5000
total_salary = 0
bonus = 0.3
is_bonus = input("Does the employee receive the bonus? (Yes/No): ") == "Yes" #wartosc boolean. Porównuje nam lewą strone z prawa. Jesli lewa rowna sie prawej to zwraca wartosc True a jesli nie to False

if is_bonus:
    total_salary = basic_salary*bonus + basic_salary
else:
    total_salary = basic_salary

print(f"Basic salary: {basic_salary}")
print(f"Bonus included? {is_bonus}")
print(f"Total salary: {total_salary}")