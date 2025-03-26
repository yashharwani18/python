import random
lst = random.sample(range(-15, 16), 10)
total = list(map(lambda x:x*x,lst))
print(lst)
print(total)