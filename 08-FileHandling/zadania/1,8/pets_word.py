#Napisz program, który drukuje tekst i zlicza liczbę słów w tekście.


import os #modul ktory sluzy do pracy z folderami, sciezkami

# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def read_from_file(name): #wczytuje caly plik i zwraca jego zawartosc
    with open(name, 'r') as file:
        content = file.read() #zawartosc pliku jako jeden dlugi napis
    return content

file_content = read_from_file('pets.txt') #cała zawartość pets.txt jako jeden napis
file_lines = file_content.splitlines() #dzielimy nasz tekst na linie/wiersze

word_count = 0 #licznik slow w tekscie
for line in file_lines: #przeszukujemy kazde kazda linie w liscie
    words = line.split() #dzieli napis na osobne slowa
    word_count += len(words) #zwiekszamy licznik slow, len(words) to liczba slow w danej linii

print("Number of words: ",word_count)
