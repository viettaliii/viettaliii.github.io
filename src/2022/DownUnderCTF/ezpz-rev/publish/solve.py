str1 = '5a4b3c2d5a4b4c1d2a1e3a3b4c1d2a1e1f2a3b3c1g1d3e5f1b2c2g1d1f2e4f6g1d7f3h3g1d4f6h3g1d2f1i4j1h2k2l1m1d3i2j5k2l2m2i3j4k3l2m2i3j4k3l2m1i5j2k2n2l2m1i4j5n4l'

lst1 = []
for i in str1:
    lst1.append(str(hex(ord(i))[2:]))

# print(lst1)

for i in lst1:
    i_int = int(i, 16) 
    if i_int> int('30',16):
        i = str(hex(i_int - int('31',16))[2:])
        print(i, end=" ")
# print(lst1)
