#Palindrom to wyrażenie, które brzmi tak samo, gdy czyta się je od tyłu
#Zdefiniuj funkcje, która zwraca wartość True, jeśli wyrażenie jest palindromem, lub False w przeciwnym wypadku.
def f(palindrome):
    text = palindrome[::-1] #to odwrocenie tekstu
    if palindrome == text: #jesli nasz wprowadzony text jest taki sam jak text odwrocony
        return True #zwracamy true
    else:
        return False

palindrome = input("Enter word: ")
print(f(palindrome))