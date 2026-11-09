###
#Program oblicza i wyświetla:
#Liczbę osób i odsetek ogółu ludności zamieszkującej półkulę północną
#Liczbę osób i odsetek ogółu ludności zamieszkującej półkulę południową
#

total = 8000000000 #suma ludności obu półkul
north = 7200000000 #liczba ludności półkuli północnej
south = total - north #ludność na półkuli południowej
print("World population: ",total)
print("North Hemisphere: ", north)
print("South Hemisphere: ",south)
print("Northern Hemisphere in %: ",(north/total)*100) #odsetek ludności półkuli północnej
print("Southern Hemisphere in %: ",(south/total)*100)