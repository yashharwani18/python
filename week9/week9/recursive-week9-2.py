def binary_equivalent(n):
    if n ==0:
        return "" 
    if n % 2 ==0:
        return "0"+binary_equivalent(n//2)
    elif n % 2 !=0:
        return "1"+binary_equivalent(n//2)
num = int(input("Enter a positive integer: "))
print(binary_equivalent(num)[::-1])