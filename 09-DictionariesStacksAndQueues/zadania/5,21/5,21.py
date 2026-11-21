import json

book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genre": "dystopian fiction",
    "pages": 328
}

with open('favourite.json', 'w', encoding = 'UTF-8') as file:
    json.dump(book, file, indent=4) #wciecia po 4 spacje