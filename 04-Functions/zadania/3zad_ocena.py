###
# Calculates the final grade for a test based
# on the number of points obtained
#

def points_to_grade(points):
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
grade = points_to_grade(test_points)
print(f"You scored: {test_points}. Your final grade is: {points_to_grade(test_points)}")