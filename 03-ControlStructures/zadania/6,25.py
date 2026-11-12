#Program tworzy wzor
for i in range(1,10): #petla wykona sie 9 razy
    for j in range(i): #petla wewnetrzna wykona sie tyle razy ile wynosi i
        print(i, end="") #program wyswietla liczbe i, end="" oznacza, ze po wyswietleniu liczby nie przechodzi do nowej linii
    print()