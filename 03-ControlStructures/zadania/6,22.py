
i = 0 #nasza liczba, narazie wynosi 0
for i in range(1,31): #petla wykona sie 30 razy w zakresi liczb od 1 do 30
    if i % 3 == 0 and i % 5 == 0: #jesli liczba jest podzielna przez 3 i 5
        print("Bingo")
    elif i % 3 == 0:
        print("Three")
    elif i % 5 == 0:
        print("Five")
    else: #a jesli liczba nie jest podzielna ani przez 3 ani przez 5 to wyswietlamy ja cyfrowo a nie slownie
         print(i)


