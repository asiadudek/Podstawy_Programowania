###
# Calculates the total value of money spent
#Plik report.txt zawiera wiadomość e-mail z raportem zakupów. 
# Napisz program, który oblicza całkowitą wartość wydanych pieniędzy.


import re #modul do wyrazen regularnych, sluzy do szukania za pomoca wzorow w tekscie
import os #modul ktory sluzy do pracy z folderami, sciezkami

# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, "r", encoding = 'UTF-8') as file:
   email = file.read() #cala zawartosc pliku, jako jeden dlugi napis

# regular expression pattern
# for amounts
# pattern - wzorzec do szukania kwot
# € - dosłowny znak euro
# \d - jedna cyfra (0-9)
# + - poprzedni element jeden lub więcej razy, więc \d+ to liczba o dowolnej długości
# ( ) - nawiasy oznaczają "zapamiętaj tylko tę część"; findall zwróci same cyfry, bez znaku €
# Razem: znajdź € i zapamiętaj liczbę, która po nim stoi, np. z "€25" zapamięta "25"
pattern = r'€(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email) #znajduje wszystkie fragmenty pasujące do wzoru

# calculate the total purchases
total = 0 #calkowita wartosc wydanych pieniedzy
for amount in amounts: #przeszukuje elementy z elementow pasujacych do wzoru
   total += int(amount) #zamienia napis na liczbe calkowita i dodajemy ja do sumy

# print result
print(total)