def count_alpha_digits(s):
    result = {"alphabets":0,"digits":0}
    for c in s:
        if c.isalpha():
            result["alphabets"]+=1
        elif c.isdigit():
            result["digits"]+=1
    print(result)
s = input()
count_alpha_digits(s)

