f =open("encoded_flag3",'r', encoding='cp437')
flag_encode = f.read()
# print(flag_encode)
lst1 = []
for i in flag_encode:
    lst1.append(ord(i))
print(lst1)
for i in range(0,len(lst1),2):
    print(chr(lst1[i]^lst1[i+1]),end='')


