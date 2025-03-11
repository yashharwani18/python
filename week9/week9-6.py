def create_tuple_list(end):
    return[(x,x**2,x**3) for x in range(1,end+1)]
end=int(input())
print(create_tuple_list(end))
