def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    sum_div = 0
    for i in range(1, n // 2 + 1): 
        if n % i == 0:
            sum_div += i
    return sum_div == n  

def is_armstrong(n):
    num_str = str(n) 
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)  
    return total == n

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_automorphic(n):
    square = str(n * n)
    return square.endswith(str(n))

num = int(input("Enter a number: "))
print(f"Is {num} a prime number? {is_prime(num)}")
print(f"Is {num} a perfect number? {is_perfect(num)}")
print(f"Is {num} an Armstrong number? {is_armstrong(num)}")
print(f"Is {num} a palindrome? {is_palindrome(num)}")
print(f"Is {num} automorphic? {is_automorphic(num)}")
