def convert(sentence):
    words = sentence.split()
    unique = set(words)
    sort = sorted(unique)
    return ' '.join(sort)
string = input()
result = convert(string)
print(result)
