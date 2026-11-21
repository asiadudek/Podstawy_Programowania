#wydrukuje imię, nazwisko i adres e-mail (w podanej kolejności, bez tytułu stanowiska) 



import csv #modul do  odczytu plikow csv

job_title = 'Graphic Designer'
print("GRAPHIC DESIGNERS")
print("=================")

with open('it_company.csv', 'r') as file:
    reader = csv.reader(file) #czytnik dzieli kazda linie na kolumny
    for row in reader: #przeszukujemy kazdy wiersz w pliku
        first_name = row[1]
        last_name = row[0]
        email = row[3]
        title = row[2]
        if title == job_title:
            print(f"{last_name} {first_name} {email}")





