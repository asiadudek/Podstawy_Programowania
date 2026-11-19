person = {
   "name": "Marek", #typ string
   "surname": "Banach", #typ string
   "age": 25, #typ int
   "hobby": ["swimming","excursions"], #typ lista
   "married": True, #typ bool
   "phone":{"landline":"123444321","mobile":"777888999"} #slownik
}

print(person['name'])
print(person['hobby'])
print(person)
person['surname'] = 'Nowak'
person['married'] = False
person ['gender'] = "Male"
person['hobby'].append('bicycle')
person['phone']['work'] = '313131444'
print(person)

for key,value in person.items():
    print(key,':', value)