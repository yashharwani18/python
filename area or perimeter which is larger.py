def area(length,breadth):
    area = length*breadth
    return area
def perimeter(length,breadth):
    perimeter = length*2+breadth*2
    return perimeter

def which_is_larger(perimeter, area):
    if area > perimeter:
        return f"area is greater than perimeter"
    else:
        return f"perimeter is greater than area"


length = int(input("enter length"))
breadth = int(input("enter breadth"))
a = area(length, breadth)
b = perimeter(length, breadth)
print(a,b)
print(which_is_larger(b,a))
