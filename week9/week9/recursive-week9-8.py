def string_length(s):
    if s =="":
        return 0
    return 1+string_length(s[1:])
    
s = input("Enter a string: ")
print(string_length(s)) 