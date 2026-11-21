#Napisz program, który oblicza liczbę wierszy, znaków i słów dla dowolnego pliku tekstowego. Użytkownik wprowadza nazwę pliku z klawiatury.
#Użyj bloku try-except, aby uniknąć przerwania programu, gdy użytkownik wprowadzi nazwę pliku, która nie istnieje.
#Wydrukuj wynik obliczeń

import csv

file_name = input("Enter file name: ")

try: #próbujemy wykonać kod, który może zgłosić błąd
    with open(file_name, 'r', encoding = 'UTF-8') as file:
        content = file.read() #zawartosc pliku

    lines = content.splitlines() #dzieli tekst na listę wierszy
    words = content.split() #dzieli tekst na listę słów (po spacjach i enterach)
    characters = len(content) #len tekstu = liczba wszystkich znaków (ze spacjami i enterami

    print("Number of lines: ",len(lines))
    print("Number of words: ", len(words))
    print("Number of characters: ", characters)

except FileNotFoundError: #wykona się tylko, gdy pliku o takiej nazwie nie ma
    print("File not found.") #komunikat zamiast przerwania programu przez błąd