ntuple=(1,2,3,4)
temp_list = list(ntuple)
temp_list[2]=10000
ntuple = tuple(temp_list)
print(ntuple)
