list_1 = [5,5,8,6,3,24,4]
list_2 = [8,78,3]
sort = []
isSorted = False
count  = 0

#merge = list_1.append(list_2)

for element in list_1:
    list_2.append(element)

res =  list_2.sort()
print(list_2)



'''
index_1 =0 
index_2 = 0
while (index_1 < len(list_1) and index_2 < len(list_2)):
    if list_1[index_1] < list_2[index_2]:
        sort.append(list_1[index_1])
        index_1 += 1
    else:
        sort.append(list_2[index_2])
        index_2 += 1
        
    print(sort)

print(len(list_1)+len(list_2))
print(len(sort))
'''
    


