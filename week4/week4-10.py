def generate_fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_series = generate_fibonacci(n)
print("Fibonacci series:", fib_series)
