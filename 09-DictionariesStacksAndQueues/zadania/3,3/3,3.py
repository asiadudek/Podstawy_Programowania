#Zdefiniuj funkcję, która zwraca wartość true, jeśli nawiasy() ,{} ,[] są poprawnie użyte w danym wyrażeniu. W przeciwnym wypadku funkcja zwraca wartość false. 

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression): #expression - tekst z wyrażeniem do sprawdzenia
    stack = [] #stos na otwierające nawiasy, na start pusty
    pairs = {')': '(', ']': '[', '}': '{'} #zamykajacy - otwierajacy
    for char in expression:
        if char in "([{": #to nawias otwierajacy
          stack.append(char) #kładzie go na stos (czeka na swój zamykający)
        elif char in ')]}':  #to nawias zamykajacy
          if len(stack) == 0 or stack.pop() != pairs[char]: #nie ma żadnego otwartego nawiasu do zamknięcia -> błąd lub nawiasy nie pasuja do siebie
            return False #od razu konczymy z False
    return len(stack) == 0  #True tylko gdy na stosie nic nie zostało (każdy nawias został zamknięty)

if brackets_ok(expression1):
   print("Expression 1: brackets are OK")
else:
   print("Expression 1: brackets are not correct")

if brackets_ok(expression2):
    print("Expression 2: brackets are OK")
else:
   print("Expression 2: brackets are not correct")

if brackets_ok(expression3):
   print("Expression 3: brackets are OK")
else:
   print("Expression 3: brackets are not correct")