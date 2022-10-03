license_enc = input("\nInput lincense encode: ")
# license_enc = "51c49a1a00647b037f5f3d5c878eb656"

lst_lin_enc = [9]
for i in license_enc:
    lst_lin_enc.append(int(i,16))

# [9, 5, 1, 12, 4, 9, 10, 1, 10, 0, 0, 6, 4, 7, 11, 0, 3, 7, 15, 5, 15, 3, 13, 5, 12, 8, 7, 8, 14, 11, 6, 5, 6]

lst = []
for i in range(len(lst_lin_enc)-1,0,-1):
    temp = lst_lin_enc[i]-lst_lin_enc[i-1]
    if temp <0:
        temp += 16
    lst.append(temp)
print("License: ", end='')
print(''.join(hex(i)[2:] for i in lst)[::-1]) 