code_enc = "052f72490451065653500357000307055007010b090d0a0055030704530a020c07510652080f0c01060f0701050f50080509020b540a015e04540456565756500605482529"

lst_code_enc = []
for i in range(0,len(code_enc),2):
    lst_code_enc.append(abs(int(code_enc[i:i+2],16)-100))



def encode(dest):
    lst = [0]*69
    for i in range(0,68):
        lst[i] = (dest[i] >> 4) | int(str(dest[i+ 1] << 4)[-2:],10)
    lst[68] = (dest[68] << 4) | ( dest[0] >> 4 & 15)

    lst1 = []
    for i in range(69):
        lst1.append(dest[i] ^lst[i])

    return lst1

def encode_short(dest):
    lst1 = []
    temp = dest[0]
    for i in range(68):
        lst1.append(dest[i] ^((dest[i+1] >> 4) | (16 * dest[i])))
    lst1[68] = dest[68]^((temp >> 4) & 15 | (16 * dest[68]))
    return lst1


def tao_ham(a):
    for i in range(64):
        

lst_s = lst_code_enc
lst_s = encode(lst_s)
lst_s = encode(lst_s)
lst_s = encode(lst_s)
lst_s = encode(lst_s)
if lst_s == lst_code_enc:
    for i in lst_s:
        print(chr(i),end='')
