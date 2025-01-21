def check_triangle(a,b,c):
    if a+b+c == 180:
        return f"valid triangle"
    else:
        return f"not valid triangle"


a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
print(check_triangle(a,b,c))

