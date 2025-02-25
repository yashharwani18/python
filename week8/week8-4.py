names = {"Alice","Ashit","Ansh","Bhavya","Bob","Bhagya"}
namesA={name for name in names if name.startswith("A")}
namesB={name for name in names if name.startswith("B")}
print("names that start with A:",namesA)
print("names that start with B:",namesB)
