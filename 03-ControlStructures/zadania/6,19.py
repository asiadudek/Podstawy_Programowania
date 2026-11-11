
print("SURVEY")

question1 = input("Are you interested in computer science? (y/n): ")
question2 = input("Do you like playing computer games (y/n): ")
question3 = input("Do you have an Instagram account? (y/n): ")

if question1 == "y":
    question1 = "yes"
else:
    question1 = "no"

if question2 == "y":
    question2 = "yes"
else:
    question2 = "no"
    
if question3 == "y":
    question3 = "yes"
else:
    question3 = "no"

print("SURVEY RESULTS")

print(f"Interested in computer science: {question1}")
print(f"Playing computer games: {question2}")
print(f"Has an Instagram account: {question3}")
