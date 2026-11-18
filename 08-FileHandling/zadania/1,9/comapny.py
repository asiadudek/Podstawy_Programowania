###
# Prints employees employed in a specified position.
# Napisz program, który wyświetla tylko pracowników ze stanowiskiem "Inżynier oprogramowania". Numeruj pozycje na drukowanej liście.

import os #modul ktory sluzy do pracy z folderami, sciezkami

# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Employee List
file_name = 'it_company.csv' #nazwa pliku z danymi wszystkich pracowników

# Position
job_title = 'Software Engineer' #szukane stanowisko (napis, którego szukamy w każdej linii)

counter = 1 #licznik
with open('it_company.csv', 'r') as file:
   for line in file: #przeszukujemy kazda linie w pliku
      if job_title in line: #jesli znajdziemy taki tytul w danej linii
        print(counter, line, end='') #wypisujemy go razem z numerem
        counter  += 1 #po sprawdzeniu danej linii i znalezieniu takiego tytulu zwiekszamy licznik o 1