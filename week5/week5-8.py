from collections import deque
queue=deque()
number_of_elements=int(input("how many number of elements in the queue"))
while True:
    choice = input("what to do?")
    if choice =='1':
        if len(queue)>=number_of_elements:
            print("queue is full")
            continue
        temp_value=input("what number do you want to add")
        queue.append(temp_value)
    elif choice=='2':
        try:
            queue.popleft()
        except:
            print("queue is empty")
    elif choice=='3':
        break
    else:
        continue
    print(list(queue))
