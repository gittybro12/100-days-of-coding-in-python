student_score = {
    'harry':81,
    'ron': 78,
    'hermione':99,
    'draco': 74,
    'neville':62,
}
student_grade ={}
for x in student_score:
    score = student_score[x]
    if score >= 91 and score <= 100:
        student_grade[x] = "Outstanding "
    elif score >=81 and score <=90:
        student_grade[x] = 'Exceeds Expectation'
    elif score >= 71 and score <=80:
        student_grade[x] = 'Acceptable'
    else:
        student_grade[x] = 'Fail'  
print(student_grade)
    
for i in student_score:
    print(i)