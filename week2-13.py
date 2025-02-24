def number_to_word(n):
    if 0<=n<=19:
        word = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", 
            "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        ]
        return word[n]
    else:
        return "out of range"

n = int(input("enter n"))
print(number_to_word(n))
