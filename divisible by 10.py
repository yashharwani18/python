def divisible_by_10(a):
    if a % 10 == 0:
        return f"{a} is divisble by 10"
    else:
        return f"{a} is not divisble by 10"


a = int(input("enter a: "))
print(divisible_by_10(a))

