#Napisz program, który tworzy słownik o nazwie person zawierający dane z dwóch pozostałych słowników (pięć par klucz-wartość).

basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

person = {} #nowy slownik

for key, value in basic_data.items(): #.items zwraca pary
    person[key] = value #key to klucz a value to przypisana wartosc do niego, dodaje do person klucz key z wartością value (kopiuje parę)

for key,value in advanced_data.items():
    person[key] = value
    

print(person)