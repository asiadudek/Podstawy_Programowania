



import csv #modul do  odczytu plikow csv
import os #modul ktory sluzy do pracy z folderami, sciezkami
# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

job_title = 'Graphic Designer'
print("GRAPHIC DESIGNERS")
print("=================")

with open('it_company.csv', 'r') as file:
    reader = csv.reader(file) #czytnik dzieli kazda linie na kolumny
    for row in reader: #przeszukujemy kazdy wiersz w pliku
        last_name = row[0]
        first_name = row[1]
        email = row[3]
        title = row[2]
        if title == job_title:
            print(f"{last_name} {first_name} {email} {title}")





