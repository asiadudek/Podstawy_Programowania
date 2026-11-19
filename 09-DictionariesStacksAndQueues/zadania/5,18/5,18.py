import json
with open('dogs.json', 'r', encoding = "UTF-8") as file:
    data = json.load(file)
    for dog in data:
        if int(dog['age']) < 5:
            for key,value in dog.items():
                print(key, ":", value)
        print()