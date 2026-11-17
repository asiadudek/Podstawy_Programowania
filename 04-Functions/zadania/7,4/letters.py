

def count_letter(text, letter):
    counter = 0 #licznik

    for char in text:
        if char == letter:
            counter += 1
    return counter