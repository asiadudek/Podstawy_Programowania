###
# Calculates the total value of money spent
#Plik report.txt zawiera wiadomość e-mail z raportem zakupów. 
# Napisz program, który oblicza całkowitą wartość wydanych pieniędzy.


import re #modul do wyrazen regularnych, sluzy do szukania za pomoca wzorow w tekscie


# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, "r", encoding = 'UTF-8') as file:
   email = file.read() #cala zawartosc pliku, jako jeden dlugi napis

# Razem: znajdź € i zapamiętaj liczbę, która po nim stoi, np. z "€25" zapamięta "25"
pattern = r'€(\d+)'

amounts = re.findall(pattern, email) #znajduje wszystkie fragmenty pasujące do wzoru

total = 0 #calkowita wartosc wydanych pieniedzy
for amount in amounts: 
   total += int(amount) #zamienia napis na liczbe calkowita i dodajemy ja do sumy

print(total)