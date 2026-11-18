#Napisz program, który kopiuje dane książki z danego gatunku do odpowiadającego mu pliku.

import csv
import os #modul ktory sluzy do pracy z folderami, sciezkami
# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def read_books(file):
    with open(file, 'r', encoding = 'UTF-8') as file:
        reader = csv.reader(file) #czytnik, dzieli każda linie na kolumny
        next(reader) #pomija nagłowek
        return list(reader) #zamienia wiersze na liste
    
def copy_genre(book, genre): #book to tutaj lista naszych wierszy w liście
    file = 'books_'+ genre.lower()+".txt" #budujemy nazwe pliku
    with open(file, 'a', encoding = 'UTF-8') as file: #dopisujemy na koncu pliku "a" dopisuje na koncu
        file.write(str(book) + '\n') #zamieniamy nasze wiersze na tekst i dodajemy do listy

books = read_books('books.csv') #cala lista ksiazek z pliku

for book in books: #book to kolejny wiersz, petla sprawdza po kolei kazda
    genre = book[2] #gatunek znajduje sie na 3 miejscu to kolumna[2] z tego wiersza
    copy_genre(book, genre) #zapisujemy dany wiersz do pliku do odpowiedniego gatunku





