#Napisz program do tłumaczenia słów z angielskiego na polski. Użytkownik wprowadza słowo w języku angielskim z klawiatury. 
#Program wyświetla tłumaczenie słowa lub informację, że tłumaczenie jest niedostępne.


translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

word = input("Enter word in English: ")

if word in translations:
    print(translations[word]) #zwraca wartosc przypisana do tego klucza
else:
    print("Translation are not available")