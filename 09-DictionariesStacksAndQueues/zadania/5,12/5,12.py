#Zdefiniuj funkcję, która przyjmuje ciąg znaków jako dane wejściowe i używa stosu do jego odwrócenia. Następnie napisz program, który odwróci tekst wprowadzony z klawiatury.

def reverse_text(text): 
    stack = [] 
    for char in text:
        stack.append(char)  #kladziemy litere na wierzch stosu

    reversed_text = '' #miejsce na nasz odrócony text
    
    while len(stack) > 0:#pętla powtarza się dopóki w stosie cos jest
        reversed_text += stack.pop() 
    return reversed_text

word = input("Enter text:" )
print(reverse_text(word))