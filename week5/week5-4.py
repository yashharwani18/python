import random
list=[random.randrange(-15,15) for _ in range(30)]
poslist=[]
neglist=[]
for num in list:
    if num >0:
        poslist.append(num)
    if num<0:
        neglist.append(num)
print(poslist)
print(neglist)
