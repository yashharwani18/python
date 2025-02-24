def is_collinear(x1,x2,x3,y1,y2,y3):
    if (y2-y1)/(x2-x1)==(y3-y2)*(x3-x2):
        return f"collinear"
    else:
        return f"not collinear"


x1 = int(input("enter x1"))
x2 = int(input("enter x2"))
x3 = int(input("enter x3"))
y1 = int(input("enter y1"))
y2 = int(input("enter y2"))
y3 = int(input("enter y3"))
print(is_collinear(x1,x2,x3,y1,y2,y3))

