
def f(name):
    result = ""#od tego zaczynamy, nic tu narazie nie ma
    for word in name.split():# name.split() dzieli nam tekst na poszczegolne litery osobno
        result = result + word[0]
    return result


name = input("Enter name: ")
print(f(name))
