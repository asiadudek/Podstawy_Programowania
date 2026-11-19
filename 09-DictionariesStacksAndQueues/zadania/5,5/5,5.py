#Napisz program, który zlicza, ile razy każde słowo pojawia się w akapicie.


paragraph = "cat dog mouse cat rat cat mouse"

counter = {} #to nasz pusty słownik na wyniki
for word in paragraph.split(): #paragraph.split() dzieli nam calą linijke tesktu na poszczególne wyrazy
    if word in counter: #sprawdzamy czy nasze słowo już sie powtórzylo
        counter[word] += 1
    else:
        counter[word] = 1
print(counter)