students = [
    (101, "Yash", 18),
    (102, "Narendra", 19),
    (103, "Ishika", 20),
    (104, "Sneha", 18),
    (105, "Sheesh", 21)
]

rollno = [student[0] for student in students]
names = [student[1] for student in students]
age = [student[2] for student in students]

print("Roll Numbers:", rollno)
print("Names:", names)
print("Ages:", age)