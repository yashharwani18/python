names=set()
names.update(["yash","mahir","ansh","nishant","narendra"])
print(names)
if "yash" in names:
    names.remove("yash")
    names.add("better yash")

print(names)

names.discard("better yash")
names.discard("mahir")

print(names)
