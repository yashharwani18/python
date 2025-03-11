def ispangram(sentence):
    alphabet_set=set('abcdefghijklmnopqrstuvwxyz')
    sentence_set=set(sentence.lower())
    return alphabet_set<=sentence_set
sentence="The quick brown fox jumps over the lazy dog"
print(ispangram(sentence))
