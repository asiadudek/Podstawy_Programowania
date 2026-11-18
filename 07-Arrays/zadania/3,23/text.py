#Zmienna zawiera tekst
#Utwórz moduł MyText zawierający:

#Funkcja zwracająca liczbę słów w tekście
#Funkcja zwracająca uporządkowaną tablicę słów, od najdłuższego do najkrótszego
#Funkcja zwracająca alfabetycznie uporządkowaną tablicę słów


import Mytext

text = "An apple a day keeps the doctor away"
print(text)
print("Counted Words: ", Mytext.count_words(text))
print("Split words: ", Mytext.word(text))
print("The length of words: ",Mytext.length_words(text))
print("Words alphabetically: ", Mytext.words_alphabetically(text))