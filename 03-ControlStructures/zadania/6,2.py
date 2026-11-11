###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU" #nasze samogloski
vowel_count = 0 #licznik samoglosek

# Count vowels in the text
i = 0 #i oznacza pozycje danego znaku w tekscie
while i < len(text): #petla wykonuje sie dopoki i czyli pozycja znaku w tekscie jest mniejsza od calkowitej dlugosci tekstu czyli ostatniej litery
    char = text[i] #char to litera w tekscie na pozycji i
    if char in vowels: #petla ktora sprawdza czy dana litera w tekscie jest samogloska
        vowel_count += 1 #jesli dana litera jest samogloska to zwiekszamy licznik samoglosek o 1
    i += 1 #przechodzimy do kolejnej litery w tekscie, dlatego zwiekszamy pozycje o 1 i przesuwamy sie w prawo

print(f"The number of vowels in the text is: {vowel_count}")