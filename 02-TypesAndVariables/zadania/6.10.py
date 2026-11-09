###
# String manipulation
#
movie = "The Lord of the Rings: The Return of the King"
# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print("Title in capital letters: ",movie.upper())

# print title in small letters
print("Title in small letters: ",movie.lower())

# print how many times the vowel "e" appears in the title
print("The letter e appears: ", movie.count("e"),"times")

# print where in the text is the word "Lord"
print("Lord is at index: ",movie.find("Lord")) #znajduje nam szukane slowo

# print where in the text is the word "dragon"
print("Dragon is at index: ",movie.find("dragon")) #wyswietla wartosc -1 bo w tekscie nie ma takiego wyrazu