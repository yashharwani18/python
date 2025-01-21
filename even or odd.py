def even_or_odd(a):
    if a % 2 == 0:
        return f"{a} is even"
    else:
        return f"{a} is odd"


a = int(input("enter a"))
print(even_or_odd(a))

