
def f(text):
    result = ""
    for char in range(len(text)):
        if char > 0:
            result = result + "-"
        result = result + text[char]
    return result


text = input("Enter text: ")
print(f(text))