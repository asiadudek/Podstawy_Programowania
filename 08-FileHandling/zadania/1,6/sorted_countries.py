###
# Reads the entire contents of a file
# Zmodyfikuj program, aby wydrukować listę krajów posortowaną alfabetycznie.
import os #modul ktory sluzy do pracy z folderami, sciezkami

# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def read_from_file(name): #Funkcja wczytuje cały plik i zwraca jego zawartość
    with open(name, 'r') as file:
        content = file.read() #wyswietlamy zawartosc pliku jako jeden dlugi napis
    return content

# reads the entire file
file_content = read_from_file('countries.txt') #cała zawartość pliku countries.txt jako jeden napis

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines() #dzieli napis na osobne linie
sorted_lines = sorted(file_lines) #sortujemy nasza zawartosc

# prints the array
for line in sorted_lines:
   print(line)


