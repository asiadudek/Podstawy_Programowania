import json
import os #modul ktory sluzy do pracy z folderami, sciezkami

# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genre": "dystopian fiction",
    "pages": 328
}

with open('favourite.json', 'w', encoding = 'UTF-8') as file:
    json.dump(book, file, indent=4) #wciecia po 4 spacje