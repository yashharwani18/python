string = input("enter string")
char={}
for i in string:
    if i in char:
        char[i]+=1  
    else:
        char[i]=1 
print(char)