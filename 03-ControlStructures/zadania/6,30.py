#Kupon loteryjny w zakresie liczb: 1 do 49

for i in range(1,8): #Odpowiada za to w ktorej linijce jestesmy.Zmienia sie dopiero jak petla wewnetrzna skonczy swoje 7 obrotow
    for j in range(7): # Odpowiada za to co dopisujemy w linijce w ktorej aktualnie sie znajdujemy
        print(i + 7*j, end=" ") 
    print()