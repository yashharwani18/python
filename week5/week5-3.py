import random
list=[random.randrange(1,30) for _ in range(50)]
uniquelist=[]
for num in list:
    if num not in uniquelist:
        uniquelist.append(num)
print(list)
print(uniquelist)
