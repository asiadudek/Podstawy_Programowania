#Poniższy program identyfikuje studentów, którzy są nieobecni. 

all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

absent_students = all_students - attended_students  # Difference
print(absent_students)