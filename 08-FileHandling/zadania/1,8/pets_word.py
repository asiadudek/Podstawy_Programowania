#Napisz program, który drukuje tekst i zlicza liczbę słów w tekście.

with open('pets.txt', 'r') as file:
    content = file.read()

lines = content.splitlines() #dzielimy nasz tekst na linie/wiersze

word_count = 0 #licznik slow w tekscie
for line in lines: #przeszukujemy kazde kazda linie w liscie
    words = line.split() #dzieli napis na osobne slowa
    word_count += len(words) #zwiekszamy licznik slow, len(words) to liczba slow w danej linii

print("Number of words: ",word_count)
