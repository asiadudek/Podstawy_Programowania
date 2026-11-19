#Napisz program, który oblicza i wyświetla średnią cenę pokoju w hotelach w Krakowie i Sopocie oraz wskazuje, w których miastach hotele są tańsze. 


hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]


def hotel_list(hotels):
    result = '' #nowy tekst do ktorego bedziemy wrzucac nazwy hoteli
    for hotel in hotels: #bierzemy kazdy po kolei hotel z listy
        if result != "": #sprawdzamy czy mamy już coś w naszym tekscie
            result += ',' #jesli mamy to dodajemy przecinek
        result += hotel['name'] #a jesli nic nie mamy to dodajemy nazwe hotelu
    return result

    
def avg_price(hotels):
    total = 0 #suma cen hoteli
    for hotel in hotels:
        total += hotel['price']
    return round(total / len(hotels),2)

avg_price_krakow = avg_price(hotels_in_Krakow)
avg_price_sopot = avg_price(hotels_in_Sopot)

print("Hotels in Krakow:", hotel_list(hotels_in_Krakow))
print("Average hotel price in Krakow:", avg_price_krakow)
print("Hotels in Sopot:", hotel_list(hotels_in_Sopot))
print("Average hotel price in Sopot:", avg_price_sopot)

if avg_price_sopot < avg_price_krakow:
    print("Hotels in Sopot are cheaper")
else:
    print("Hotels in Krakow are cheaper")
    



