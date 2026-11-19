# Wyświetl ostatnie dziesięć kursów wymiany euro w formacie json w przeglądarce internetowej.

import json
import os #modul ktory sluzy do pracy z folderami, sciezkami

# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open ("euro.json", "r", encoding = "UTF-8") as file:
    counter = json.load(file) #nasza zawartosc pliku

print("Date            Buying Rate     Selling Rate") #tworzymy naglowek, data, kurs kupna, kurs sprzedazy
print("============================================")

# data["rates"] to lista 10 dni
# w każdym obrocie pętli rate to jeden dzień
for rate in counter["rates"]:
    print(rate["effectiveDate"], "        ", rate["bid"], "         ", rate["ask"])
