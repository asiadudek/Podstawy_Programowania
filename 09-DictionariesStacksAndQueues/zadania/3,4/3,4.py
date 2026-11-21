#Napisz program, który konwertuje dowolną liczbę naturalną na liczbę binarną. 

number = int(input("Enter number: "))
stack = [] #puste miejsce na stosie, miejsce na reszty z dzielenia

while number > 0: #dopoki liczba jest wieksza od 0
    rest = number % 2
    stack.append(rest) #kladziemy reszte z dzielenia na stos
    number = number // 2 #dzielenie calkowite, liczba maleje, teraz ona bedzie sprawdzana

total = '' ## tu będzie wynik jako tekst, na start pusty
while stack: #dopoki na stosie cos jest
    total = total + str(stack.pop()) #pop zdejmuje wierzch stosu, str zamienia cyfrę na tekst, doklejamy do wyniku

print(total)

    