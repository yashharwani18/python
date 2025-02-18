tuple_list= [(1,2),(),(3,4),(),(5,6)]
notemptylist= [i for i in tuple_list if len(i)>0]
print(notemptylist)
