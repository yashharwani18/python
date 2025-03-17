def reverse_list(n):
    if len(n)==0:
        return []
    temp = n.pop()
    reversed_part = reverse_list(n)  
    reversed_part.insert(0, temp)  
    return reversed_part 
num = list(input("Enter a positive integer: "))
print(reverse_list(num))