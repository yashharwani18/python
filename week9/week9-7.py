def ispalindrome(sentence):
    sentence = sentence.replace(" ","").lower()
    print(sentence==sentence[::-1])

sentence = input()
ispalindrome(sentence)
