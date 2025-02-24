a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
if a >= b and a >= c:
    print(a, "is the largest value")
elif b >= a and b >= c:
    print(b, "is the largest value")
elif c >= a and c >= b:
    print(c, "is the largest value")
    
if a <= b and a <= c:
    print(a, "is the smallest value")
elif b <= a and b <= c:
    print(a, "is the smallest value")
elif c <= a and c <= b:
    print(a, "is the smallest value")
