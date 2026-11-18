import re #modul wyrazen regularnych, sluzy do szukania za pomoca wzorow w tekscie
import os #modul ktory sluzy do pracy z folderami, sciezkami
# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('files.txt', 'r', encoding = "UTF-8") as file:
    content = file.read() #zawartosc pliku

# \w+        - jeden lub więcej znaków: litery, cyfry lub _ (nazwa pliku)
# \.         - dosłowna kropka (bez \ kropka oznaczałaby "dowolny znak")
# [a-z]{4}   - dokładnie 4 małe litery (rozszerzenie)
# ( )        - nawias oznacza grupę, którą findall zwraca jako wynik
pattern = r'(\w+\.[a-z]{4})' #nasz wzor
matches = re.findall(pattern, content) #findall zwraca listę wszystkich fragmentów tekstu pasujących do wzorca

for match in matches: #dla kazdego dopasowanego elementu
    print(match) #wypisujemy je na ekranie