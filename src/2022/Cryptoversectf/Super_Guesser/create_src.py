# 97 - 122
import hashlib
f = open("a.txt",'w')

for i1 in range(26):
    for i2 in range(26):
        for i3 in range(26):
            for i4 in range(26):
                for i5 in range(26):
                    f.write(str(chr(97+i1)+chr(97+i2)+chr(97+i3)+chr(97+i4)+chr(97+i5)) +'  ')
                    f.write(hashlib.md5(str(chr(97+i1)+chr(97+i2)+chr(97+i3)+chr(97+i4)+chr(97+i5)).encode()).hexdigest()+'\n')

    