#Napisz program, który rysuje wykres funkcji f(x)=x^2-3.
import matplotlib.pyplot as plt #biblioteka ktora tworzy wykresy

x = []
y = []

#create x values
for n in range(-100,101):
    x = x + [n] #dopisujemy n do listy xów, n to kolejna liczba z przedzialu -100,101

#create y values
for n in x: #n to aktualna wartosc x
    y = y + [n*n-3]

plt.plot(x,y) #przygotowuje wykres
plt.show() #otwiera okno z wykresem
