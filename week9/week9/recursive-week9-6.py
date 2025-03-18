def pos_list(lst,index=0):
    if index==len(lst):
        return lst
    if lst[index]<0:
        lst[index]=0
    return pos_list(lst,index+1)

lst=[-3,-2,-1,0,2,3]
print(pos_list(lst))
