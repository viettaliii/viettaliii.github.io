
lst1 = [8,7,5,4,1,3,2,6,9,10]
lst2 = [0,1,2,3,4,5,6,0,1,2,3,4,5,0,1,2,3,0,1,2,1]
for i in range(len(lst2)):
    temp = lst1[lst2[i]]
    lst1[lst2[i]] = lst1[lst2[i]+1]
    lst1[lst2[i]+1] = temp
print(lst1)

for i in lst2:
    print(chr(i+48),end='')