

def f(palindrome):
    palindrome = palindrome[::-1]
    return palindrome

palindrome = input("Enter word: ")
print(f(palindrome))