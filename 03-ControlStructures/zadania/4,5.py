###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#

plain_text = 'The early bird catches the worm'
encrypted_text = "" #puste miejsce na nasz zaszyfrowany tekst

for char in plain_text: #przeszukujemy każdy znak czyli litery w naszym tekście
    code = ord(char) #pobieramy kod ASCII dla każdej litery. Ord zwraca nam kod. Zamieia literę na liczbę w ASCII
    code = code + 1 #przesuwamy naszą zakodowaną literę o 1 miejsce w prawo
    new_char = chr(code) #zamieniamy nasz kod ASCII, który jest liczbą na literę. Chr zamienia liczbę na literę w ASCII
    encrypted_text = encrypted_text + new_char #do naszego miejsca na zaszyfrowany tekst dodajemy nasze zaszyfrowane litery

print(encrypted_text)