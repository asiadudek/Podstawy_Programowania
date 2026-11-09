###
# A program that prints your height both in cm and in feet and inches.
#

cm = 169
total_inches = round(cm / 2.54) # CAŁY wzrost w calach zaokraglony do liczby calkowitej (1cal = 2.54 cm)
feet = total_inches // 12 #1 stopa = 12 cali, pelne dzielenie bez reszty. sprawdzamy ile pełnych stóp mieści się w calach
inches = total_inches % 12 #liczymy cale które zostaly po obliczeniu pelnych stop, czyli reszta
print(f'I am {cm} cm tall, {feet} feet and {inches} inches')