###
# Saves to a file a list of employees working at a specified position.
#Napisz program, który zapisuje dane pracowników zatrudnionych na stanowisku 'Inżynier oprogramowania'

import os #modul ktory sluzy do pracy z folderami, sciezkami

# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r') as input_file: #czyli otwórz plik jako plik wejściowy do czytania
   with open(position_file, 'w') as output_file: #czyli utwórz lub otwórz plik wyjściowy, gotowy do zapisu danych
      for line in input_file: #sprawdzamy czy napis zawarty w job_title wystepuje gdzies wewnatrz wiersza/linii
         if job_title in line:
            output_file.write(line) #jesli jest to wypisujemy go do pliku wyjsciowego