#Plik email.txt zawiera surowy adres e-mail. Napisz program, który używa wyrażeń regularnych do pobierania i drukowania:

#adres e-mail nadawcy
#adres e-mail odbiorcy
#temat e-maila
#treść wiadomości e-mail


import re #modul z wyrazeniami regularnymi, sluzy do szukania za pomoca wzorow w tekscie


def read_from_file(email):
    with open(email, 'r', encoding = 'UTF-8') as file:
        content = file.read() #zawartosc pliku
    return content

# .*  - dowolne znaki (np. imię i nazwisko nadawcy)
# <( ... )> - adres w nawiasach <>; nawias okrągły to grupa, którą findall zwraca
# [\w.]+ - część przed @ (litery, cyfry, _ i kropki)
# @   - dosłowny znak @
# [\w]+\. - nazwa domeny i kropka
# [\w.]+  - końcówka domeny (np. com lub co.uk)

def email_sender(email): #zwraca adresata
    pattern = r'From: .*<([\w.]+@[\w]+\.[\w.]+)>'
    result = re.findall(pattern, email) #lista wszystkich dopasowań
    return result[0] #zwraca pierwszy znaleziony mail

def email_recipient(email): #zwraca adres odbiorcy
    pattern = r'To: .*<([\w.]+@[\w]+\.[\w.]+)>'
    result = re.findall(pattern, email)
    return result[0]

def email_subject(email): #zwraca temat wiadomosci
    pattern = r'Subject: (.+)' # .+ = wszystkie znaki do końca linii
    result = re.findall(pattern, email)
    return result[0]

def email_body(email):
    pattern = r'\n\s*\n([\s\S]*)' #\S to każdy znak ktory nie jest bialym \s to znak bialy, \n pusta linia, nowa linia
    result = re.findall(pattern, email)
    return result[0]
