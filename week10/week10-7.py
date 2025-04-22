import pickle
from datetime import datetime

employee = {
    "empcode": 2023,
    "empname": "Rahul Sharma",
    "date_of_joining": datetime(2021, 7, 10),
    "salary": 85000
}

with open("employee_data.pkl", "wb") as file:
    pickle.dump(employee, file)

with open("employee_data.pkl", "rb") as file:
    loaded_employee = pickle.load(file)

print("📄 Deserialized Employee Data:")
print(f"Employee Code: {loaded_employee['empcode']}")
print(f"Name: {loaded_employee['empname']}")
print(f"Date of Joining: {loaded_employee['date_of_joining'].strftime('%d-%m-%Y')}")
print(f"Salary: ₹{loaded_employee['salary']:,}")
