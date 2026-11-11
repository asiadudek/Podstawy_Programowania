###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False #False czyli wylaczone, True czyli wlaczone, dwie zarowki sa wylaczone
bulbs_on = 0 #licznik zarowek zapalonych
if light_switch1: #jesli pierwszy przelacznik jest wlaczony
    bulbs_on += 1 #zwiekszamy licznik zapalonych zarowek o 1
if light_switch2:
    bulbs_on += 2 #zwiekszamy licznik o 2 bo dwie zarowki mamy przypisane do jednej zmiennej
print(f"Number of bulbs on: {bulbs_on}")