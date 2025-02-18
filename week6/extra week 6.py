from operator import itemgetter
employees = [
    (101, 'Amit', 35, 'HR', 100000),
    (102, 'Ravi', 28, 'Finance', 12000),
    (103, 'Priya', 41, 'HR', 150000),
    (104, 'Rahul', 30, 'IT', 9000),
    (105, 'Sara', 25, 'Finance', 9500),
    (106, 'Bmit', 35, 'HR', 10000)
]

def filter_by_dept(emp_list, dept_name):
    return [emp[1] for emp in emp_list if emp[3] == dept_name]

def sort_by_salary(emp_list):
    return sorted(emp_list, key=itemgetter(4), reverse=True)
    
def find_highest_salary(emp_list):
    return max(emp_list, key=itemgetter(4))
    
def find_highest_salary_in_dep(emp_list,dept_name):
    temp_list= [emp[4] for emp in emp_list if emp[3]==dept_name]
    return max(temp_list)
    
def update_salary(emp_list,dept_id,new_salary):
    temp_list =[]
    for emp in emp_list:
        if emp[0]==dept_id:
            updated_tuple = (emp[0], emp[1], emp[2], emp[3], new_salary)
            temp_list.append(updated_tuple)
        else:
            temp_list.append(emp)
    return temp_list
    

    
dept_name=input("enter dept name")
dept_id=int(input("enter dept id"))
salary=int(input("enter salary"))
print(filter_by_dept(employees,dept_name))
print(sort_by_salary(employees))
print(find_highest_salary(employees))
print(find_highest_salary_in_dep(employees,dept_name))
updated_employees = update_salary(employees, dept_id, salary)
for emp in updated_employees:
    print(emp)
