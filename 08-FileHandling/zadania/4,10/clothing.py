#Napisz program, który drukuje te produkty, których cena jest niższa niż 60 i których zapasy są mniejsze niż 40.


import csv #modul do czytania plikow csv
import os #modul ktory sluzy do pracy z folderami, sciezkami
# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('clothing.csv', 'r', encoding = 'UTF-8') as file:
    reader = csv.reader(file) #czytnik dzieli kazda linie na kolumny
    next(reader) #pomijamy wiersz z naglowkami
    for row in reader: #przeszukujemy kazdy wiersz w pliku
        product = row[1] #row[1] to druga kolumna w wierszu
        price = float(row[5]) #zmieniamy typ ze str na float
        stock_quantity = int(row[6]) #zmieniamy typ ze str na float
        if price < 60 and stock_quantity < 40:
            print(product, price, stock_quantity)


