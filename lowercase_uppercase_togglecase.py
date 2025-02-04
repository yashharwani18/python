def lowercase(s):
    r=""
    for c in s:
        if 'A'<= c <= 'Z':
            r+=chr(ord(c)+32)
        else:
            r+=c
    return r
def uppercase(s):
    r=""
    for c in s:
        if 'a'<= c <= 'z':
            r+=chr(ord(c)-32)
        else:
            r+=c
    return r
def toggle(s):
    r=""
    for c in s:
        if 'A'<= c <= 'Z':
            r+=chr(ord(c)+32)
        elif 'a'<= c <= 'z':
            r+=chr(ord(c)-32)
        else:
            r+=c
    return r

u=input()
print(lowercase(u))
print(uppercase(u))
print(toggle(u))
        
    

