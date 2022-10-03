def rever(a1,a2):
    a = hex(a1 ^ a2)[2:]
    lst = [chr(int(a[6:8],16)),chr(int(a[4:6],16)),chr(int(a[2:4],16)),chr(int(a[:2],16))]
    return ''.join(lst)
print(rever(0x558C4DC,0x6239A8BA),end='')
print(rever(0x71100C9B,0x17F64E0),end='')
print(rever(0xCE3D1DDE,0xA14442BB),end='')
print(rever(0x322958FC,0x415C0789),end='')
print(rever(0x8CBE8F4E,0xF6E1EB2B),end='')
print(rever(0xB14A374B,0xDE2C6878),end='')
print(rever(0xEE9707A,0x669D2F08),end='')
print(rever(0xF98DDD38,0xC8D2AE51),end='')
print(rever(0x5D715F4D,0x6C12677F),end='')
print(rever(0x410B9F90,0x3C3CFBA3),end='')








