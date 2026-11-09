import random #importujemy moduł losowania

print("Rzuc kostka") 
for x in range (5): #pętla, która wykonuje się 5 razy
    rzut_kostka = random.randint(1,6) #losowanie liczb
    print("Wypadlo:", rzut_kostka) #rezultat