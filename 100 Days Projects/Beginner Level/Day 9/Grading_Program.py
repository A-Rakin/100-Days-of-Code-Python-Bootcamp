student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Shayma":92,
    "Draco":74,
    "Neville": 87
}

# Create an Empty Dictionary called Student_Grades
student_grades = {}

#Convert Scores into Grades
for student in student_scores:
    score = student_scores[student]
    if score > 90 :
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Exceptions" 
    elif score > 70:
        student_grades[student] = "Acceptable" 
    else:
       student_grades[student] = "Fail"  

print(student_grades)