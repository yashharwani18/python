import math

def point(x1,y1,x2,y2,radius):
    distance= math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    if distance < radius:
        return f"inside circle"
    elif distance == radius:
        return f"on circle"
    else:
        return f"not inside cricle"


x1 = int(input("enter circle x"))
y1 = int(input("enter circle y"))
x2 = int(input("enter point x"))
y2 = int(input("enter point y"))
radius = int(input("enter radius"))
print(point(x1,y1,x2,y2,radius))

