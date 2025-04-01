import csv
data = [
    ["name","age","chem","math","computer"]
]
for i in range(2):
    name = input("name")
    age = input("age")
    marks1,marks2,marks3 = input("marks").split()
    data.append([name,age,marks1,marks2,marks3])
with open("YOOOOOOOO.csv",mode = 'w',newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
