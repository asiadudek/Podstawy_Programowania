###
# Calculates the sum of even numbers in the range <1,10>
#

sum = 0 #zmienna przechowujaca nasza sume, narazie wynosi 0
for u in range(1,11): #przeszukujemy liczby od 1 do 10. 11 nie jest wliczana do zakresu
    if not u % 2 == 0: #jesli reszta jest rozna od 0 to znaczy ze liczba jest nieparzysta i przechodzimy do kolejnej iteracji petli
        continue #continue przerywa aktualna iteracje petli i przechodzi do kolejnej. Wtedy linijka z sum += u nie zostanie wykonana dla liczby nieparzystej
    sum += u #wyliczamy sume dla liczb parzystych

print(f"Sum of even numbers in the range <1,10) is: {sum}") 