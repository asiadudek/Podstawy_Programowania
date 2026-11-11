



for i in range(6,-1,-3): #petla zewnetrzna wykona sie od 6 do 0 ale co trzeci element. Zwraca nam 6,3,0
    for j in range(1,4): #petla wewnetrzna wykona sie od 1 do 3. Do wszystkich wartosci kolejno 6,3,0 dodajemy kolejno liczby z tej petli. Jak dodamy 1,2,3 do 6 to petla przechodzi do kolejnego wiersza
        print(f'{i+j}',end=' ') #wyswietla wynik dodawanie liczby i oraz liczby j.
    print()
