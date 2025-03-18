employees = [
    {'dept_no': 1, 'roll_no': 101, 'salary': 50000},
    {'dept_no': 1, 'roll_no': 102, 'salary': 60000},
    {'dept_no': 2, 'roll_no': 201, 'salary': 55000},
    {'dept_no': 2, 'roll_no': 202, 'salary': 75000},
    {'dept_no': 3, 'roll_no': 301, 'salary': 65000},
    {'dept_no': 3, 'roll_no': 302, 'salary': 80000}
]
dict1={}
for emp in employees:
    dept=emp["dept_no"]
    salary = emp["salary"]
    if dept not in dict1 or salary>dict1[dept]:
        dict1[dept]=salary
print(dict1)
