def count(names):
    bcount = sum(len(name) for name in names if isinstance(name,tuple))
    gcount = sum(1 for name in names if isinstance(name,str))
    print(f"boys: {bcount}")
    print(f"girls: {gcount}")
    
names = [('Darshit','Ashit','Devang'),'Ragi','Aashna','Darshini',('Darshil',)]
count(names)
