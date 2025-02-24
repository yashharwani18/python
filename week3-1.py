def count_vowel():
    user = input("enter a string")
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    count = 0
    for _ in user:
        if _ in vowels:
            count+=1
    print(f"number of vowels is {count}")

count_vowel()
    

