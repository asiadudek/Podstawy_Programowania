#narysuj linię na diagramie od pozycji (1, 3) do pozycji (8, 10).
import matplotlib.pyplot as plt #biblioteka rysujaca wykresy

xpoints = [1, 8] #pozycje naszych xow
ypoints = [3, 10] #pozycje y

plt.plot(xpoints, ypoints)
plt.show()