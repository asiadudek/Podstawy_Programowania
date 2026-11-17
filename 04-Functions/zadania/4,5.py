###
# Ocena koncowa z testu na podstawie punktow

def points_to_grade(points): #funkcja przyjmuje jeden argument czyli punkty z testu
    if points >= 18:
        grade = "Excellent"
    elif points >= 14:
        grade = "Good"
    elif points >= 10:
        grade = "Satisfactory"
    else:
        grade = "Fail"
    
    return grade
      
test_points = int(input("Enter the points: "))
grade = points_to_grade(test_points) #wywolanie funkcji
print(f"You scored: {test_points}. Your final grade is: {grade}")
    
    
    
    

    
    
    
    
    
    
    
    
    
    
   