#Napisz program, który oblicza liczbę samogłosek w tekście wprowadzanym z klawiatury. Używaj wyrażeń regularnych.

import re #modul wyrazen regularnych, sluzy do szukania za pomoca wzorow w tekscie

text = input("Enter text: ")

pattern = r'[aeiouyąęóAEIOUYĄĘÓ]' #wzorzec, oznacza dowolny znak z tego zestawu
matches = re.findall(pattern, text) #findall zwraca listę wszystkich znaków pasujących do wzorca

    
print(matches)
print("Number of vowels:",len(matches))
    
