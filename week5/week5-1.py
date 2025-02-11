import random
oddlist=[random.randrange(1,100,2) for _ in range(5)]
evenlist=[random.randrange(0,100,2) for _ in range(4)]
#for _ in range(5):
    #oddlist.append(random.randrange(1,100,2))
#for _ in range(4):
    #evenlist.append(random.randrange(0,100,2))
oddlist[2]=evenlist
finallist=[]
for _ in oddlist:
    if isinstance(_,list):
        finallist.extend(_)
    else:
        finallist.append(_)
print(sorted(finallist))
