# Wyświetl ostatnie dziesięć kursów wymiany euro w formacie json w przeglądarce internetowej.

import json

with open ("euro.json", "r", encoding = "UTF-8") as file:
    counter = json.load(file) #nasza zawartosc pliku

print("Date            Buying Rate     Selling Rate") #tworzymy naglowek, data, kurs kupna, kurs sprzedazy
print("============================================")

# counter["rates"] to lista 10 dni
# w każdym obrocie pętli rate to jeden dzień
for rate in counter["rates"]:
    print(rate["effectiveDate"], "        ", rate["bid"], "         ", rate["ask"])
