#Utwórz słownik opisujący Twój telefon komórkowy. Użyj 6 par klucz-wartość danych. Następniefor za pomocą pętli wyświetl zawartość słownika.

mobile = {
"OS":"Android",
"brand":"Realme",
"memory": "512",
"Color": "Black",
"Model": "15 pro",
"dual_sim": True 
}
for key,value in mobile.items():
   print(f"{key} : {value}")