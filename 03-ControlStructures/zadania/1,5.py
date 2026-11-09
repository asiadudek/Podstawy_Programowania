###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#

total_tasks = 20
tasks_ok = int(input("Enter your number of correct tasks: ")) #liczba zadan poprawnie wykonanych
test_passed = False #zalozenie. Na razie nie wiemy czy test jest zdany wiec False. Dopoki nie udowodnimy, ze jest zdane to uznajemy, ze jest niezdane

if tasks_ok >= total_tasks * 0.5:
    test_passed = True

if test_passed:
    print(f"Congratulations! You passed the test")
else:
    print(f"Unfortunately, you failed the test")