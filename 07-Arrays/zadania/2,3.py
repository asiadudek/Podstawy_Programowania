#Poniższe dane przedstawiają miesięczne wydatki podzielone na kategorie i tygodnie. Napisz program, który oblicza i drukuje:

#całkowite wydatki dla każdej kategorii
#całkowite wydatki na każdy tydzień
#całkowite wydatki za miesiąc


# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
expenses_food= 0 #suma wydatkow na jedzenie
expenses_transport = 0
expenses_utilities = 0
expenses_week1 = 0
expenses_week2 = 0
expenses_week3 = 0
expenses_week4 = 0


for week in monthly_expenses:
    expenses_food += week[0]
    expenses_transport += week[1]
    expenses_utilities += week[2]

for value in monthly_expenses[0]: #czyli wartosci z tygodnia pierwszego
    expenses_week1 += value

for value in monthly_expenses[1]:
    expenses_week2 += value

for value in monthly_expenses[2]:
    expenses_week3 += value

for value in monthly_expenses[3]:
    expenses_week4 += value

total = expenses_week1 + expenses_week2 + expenses_week3 + expenses_week4

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',expenses_food)
print('Transport:',expenses_transport)
print('Utilities:',expenses_utilities)
print('Week 1:',expenses_week1)
print('Week 2:',expenses_week2)
print('Week 3:',expenses_week3)
print('Week 4:',expenses_week4)
print('---------------')
print('TOTAL:',total)