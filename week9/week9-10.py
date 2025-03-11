def frequency(s):
    words = s.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    sorted_word = dict(sorted(word_count.items()))
    return sorted_word

s=input()
print(frequency(s))
