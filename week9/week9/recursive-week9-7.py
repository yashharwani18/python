def avg(lst,index=0,total=0):
    if index==len(lst):
        return total/len(lst)
    return avg(lst,index+1,total+lst[index])

lst=[1,2,3,4,5]
print(avg(lst))
