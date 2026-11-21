#Zmodyfikuj program tak, aby wydrukowana lista krajów była ponumerowana. 
with open('countries.txt', 'r') as file:
    counter = 1
    for line in file:
        print(f"{counter} {line}", end="")
        counter += 1
   

