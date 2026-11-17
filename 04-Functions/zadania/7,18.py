#Zdefiniuj funkcję zwracającą zdanie z usuniętymi spacjami.

def f(sentence):
    sentence = sentence.replace(" ","") #zamieniamy kazda spacje na pusty tekst czyli bez spacji
    return sentence


sentence = input("Enter a sentence: ")
print(f(sentence))
