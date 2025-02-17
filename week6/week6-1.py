def count(names):
    bcount = sum(1 for name in names if isinstance(name,tuple))
    gcount = sum(1 for name in names if isinstance(name,str))
    print(f"boys: {bcount}")
    print(f"girls: {gcount}")
    
names = [("Aarav",), "Anannya", ("Narendra,",), "Ishika", "Pooja", ("Rohan",), "Sneha", ("Krishna",)]
count(names)