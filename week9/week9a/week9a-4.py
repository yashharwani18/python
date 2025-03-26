lst = ['madam','Python',"malayalam",12321]
yooo = list(filter(lambda x:str(x)==str(x)[::-1], lst))
print(yooo)