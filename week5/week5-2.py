import random
f_list = []
for i in range(20):
    f_list.append(random.randrange(1,5))
inp = int(input("number"))
position=[] 
for index in range(len(f_list)):
    if f_list[index]==inp:
        position.append(index)
print(f_list)
if position:
    print(position)
