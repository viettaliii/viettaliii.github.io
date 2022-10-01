def __ROL__(num, count, bits=8):
    return ((num << count) | (num >> (bits - count))) & ((0b1<<bits) - 1)

def __ROR__(num, count, bits=8):
    return ((num >> count) | (num << (bits - count))) & ((0b1<<bits) - 1)


lst = [166, 166, 108, 226, 226, 222, 132, 188, 124, 236, 226, 120, 152, 166, 166]

for i in lst:
    for x in range(256):
        if  (i ^ 12) + 6 == __ROR__(__ROL__(x,3),2):
            print(chr(x), end="")