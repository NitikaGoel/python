students = [['Harry',37.21],['Berry',37],['Tina', 40],['Akriti',43],['Harsh',39]]
print(students[3][0])
max_grade = students[0][1]
student_name = students[0][0]
for i in students:
    if i[1] > max_grade:
        max_grade = i[1]
        student_name = i[0]
print("maxgrade is " +str(max_grade)+ " for the student " + student_name)
second_max_grade = students[0][1]
second_student_name = students[0][0]
for i in students:
    if i[1] < max_grade and i[1] > second_max_grade:
        second_max_grade = i[1]
        second_student_name = i[0]

print("Second maxgrade is " +str(second_max_grade)+ " for the student " + second_student_name)



