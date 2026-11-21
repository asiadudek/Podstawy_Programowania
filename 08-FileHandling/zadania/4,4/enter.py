#Napisz program, który wyświetla pierwsze pięć wierszy, a następnie drukuje „Naciśnij klawisz Enter...”

with open('it_company.csv', 'r', encoding = "UTF-8") as file:
     content = file.read() #zawartosc pliku

lines = content.splitlines() #dzieli tekst na liste wierszy


counter = 1 #numer wypisanego wiersza, zaczynamy od 1
for line in lines: #bierzemy po kolei kazdy wiersz
     print(counter, line) #wyswietlamy numer wiersza i wiersz
     if counter % 5 == 0: #jesli liczba dzieli sie bez reszty przez 5 to naciskamy enter
         input("Press enter")
     counter += 1 #po wypisaniu zwiekszamy numeracje wiersza o jeden dalej

     
    
     
     
    




