

def f(n):
    result = ""
    for i in range(1,n+1):
        result += str(i) #ciag znakow wiec musimy tu zrobic string
    return result

n = int(input("Enter n: "))
print(f(n), end="")