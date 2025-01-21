def check_age(a):
    if age < 18:
        return f"minor"
    else:
        return f"Major"


age = int(input("enter a: "))
print(check_age(age))

