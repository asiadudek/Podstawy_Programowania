#Utwórz tablicę zawierającą 5 słowników, z których każdy zawiera kraj i jego populację. Następnie wydrukuj zawartość tablicy
countries = [
{"name":"Poland", "population":38000000},
{"name":"Germany", "population":83200000},
{"name":"France", "population":67800000},
{"name":"Italy", "population":58900000},
{"name":"Spain", "population":49600000}
]

for country in countries:
    print(country['name'], country['population'])