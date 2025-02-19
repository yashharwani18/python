stack =[]
number_of_elements=int(input("how many number of elements in the stack"))
while True:
    choice = input("what to do?")
    if choice =='1':
        if len(stack)>=number_of_elements:
            print("stack is full")
            continue
        temp_value=input("what number do you want to add")
        stack.append(temp_value)
    elif choice=='2':
        try:
            stack.pop()
        except:
            print("stack not full")
    elif choice=='3':
        break
    else:
        continue
    print(stack)
