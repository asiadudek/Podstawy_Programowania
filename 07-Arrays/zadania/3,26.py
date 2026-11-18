#Napisz program, który rysuje funkcję y = sin(x) dla wartości kąta w zakresie 0-360 stopni.
import matplotlib.pyplot as plt #biblioteka do rysowania wykresow
import math #biblioteka z funkcjami matematycznymi

x = [] #lista kątów w stopniach
y = [] #lista wartosci sin dla tych kątów

#create values
for n in range(0,361): #n to nasz aktualny kąt w stopniach
    x = x + [n] #dopisujemy kąt do x na koniec naszej listy
    radians = math.radians(n) #zamieniamy kąt "n" w stopniach na radiany bo funkcja sin() liczy w radianach
    y = y + [math.sin(radians)] #funkcja liczy sinus kąta i dokleja go na koniec listy

plt.plot(x,y) #przygotowuje wykres 
plt.show() #otwiera okno z wykresem