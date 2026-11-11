

dog_age  = int(input("Enter dog age (in human years): "))


if dog_age <=2:
    print(f"Dog has {dog_age * 10.5} years.") #tyle przezyl w ciagu jednego roku - 10.5
else:
    print(f"Dog has {2*10.5 + (dog_age - 2)*4} years.") 
    #przez pierwsze dwa lata przezywa 10.5 lat, potem od wprowadzonego wieku psa odejmujemy 2 lata bo je mamy juz wyliczone, a pozostale mnozymy razy 4 i sumujemy