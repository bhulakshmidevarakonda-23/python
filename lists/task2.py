list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_element=[]
for i in list1:
    for j in list2:
        if i == j:
            common_element.append(i)
print(common_element)
