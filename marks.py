def grade(marks):
    if marks == "Absent":
        return "NA"
    elif 0<=marks<=39:
        return"F"
    elif 40<=marks<=44:
        return"P"
    elif 45<=marks<=49:
        return"C"
    elif 50<=marks<=54:
        return"B"
    elif 55<=marks<=59:
        return"B+"
    elif 60<=marks<=69:
        return"A"
    elif 70<=marks<=79:
        return"A+"
    elif 80<=marks<=100:
        return"O"
def avg(a,b,c):
    return (a+b+c)/3
def summ(a,b,c):
    return (a+b+c)
   
a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
print(grade(a))
print(grade(b))
print(grade(c))
print(avg(a,b,c), "is the avg")
print(summ(a,b,c), "is the sum")

if a<40 or b<40 or c<40:
    print("This student has failed")
