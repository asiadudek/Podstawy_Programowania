#Program tworzy wzor


for i in range(1,6): #petla wykona nam sie 5 razy
    for char in range(i): #znak bedzie sie powtarzal tyle razy ile wynosi i
        print("*", end=" ") #program wyswietla gwiazdki, end to znaczy obok siebie
    print() #nowa linia


for i in range (4, 0, -1): #petla wykona sie nam 4 razy od konca czyli od 4 do 1
    for char in range(i): #znak bedzie sie powtarzal tyle razy ile wynosi i
        print("*", end=" ")
    print() 
