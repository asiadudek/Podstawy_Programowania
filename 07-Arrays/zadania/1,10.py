###
# Prints test statistics
# Tablica zawiera wyniki testów ucznia. Wartość True oznacza, że uczeń odpowiedział poprawnie na pytanie, natomiast wartość False oznacza odpowiedź niepoprawną. Napisz program, który drukuje informacje o wynikach testów:

#Liczba pytań:
#Liczba poprawnych odpowiedzi:
#Liczba błędnych odpowiedzi:
#Procent poprawnych odpowiedzi:


test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results) #liczba pytan

# calculates the number of correct answers
correct_answers = 0 #licznik prawidlowych odp
for answer in test_results:
   if answer == True:
      correct_answers += 1

# calculates the number of incorrect answers
incorrect_answers = question_number - correct_answers
# calculates the percentage of correct answers
percentage = (correct_answers / question_number) *100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print("Number of incorrect answears: ", incorrect_answers)
print("Percentage of correct answears: ", round(percentage,1),"%")