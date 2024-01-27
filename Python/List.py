
# creating a student_info list to store the information about the student roll no,name, course and marks scored
Student_info = [21, 'Rose', "CSE", 30, 40, 50]
print(Student_info)

print("Student_roll :", Student_info[0], end=' , ')
print("Student_name :", Student_info[1], end=', ')
print("Student_totalMarks :", Student_info[-1], end=' ')


Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student_info[2] = "ME"
print(Student_info)


Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student_info.append(50)
print(Student_info)

Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student_info.remove(50)
print(Student_info)

Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student2_info = [22, "John", "ME", 40, 40, 50, 130]
print(Student_info + Student2_info)



