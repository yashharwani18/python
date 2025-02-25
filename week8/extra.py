list1 = [1,2,3,3,3,3,3,3]
list2 = []
print(list(set(list1)))
list
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        continue
print(list2)

