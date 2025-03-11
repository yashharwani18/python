def create_list(l1,l2):
    return list(set(list1) & set(list2))

list1=[1,2,3,4,5,3]
list2=[3,4,5,6,7]
print(create_list(list1,list2))
