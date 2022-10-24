import hashlib, re

hashes = [
 'd.0.....f5...5.6.7.1.30.6c.d9..0',
 '1b.8.1.c........09.30.....64aa9.',
 'c.d.1.53..66.4.43bd.......59...8',
 '.d.d.076........eae.3.6.85.a2...']

f = open("a.txt", 'r')

for line in f:
    if line[7] =='d' and line[9] =='0' and line[15] =='f' and line[16] == '5' and line[20]=='5' and line[22] =='6' and line[24]=='7':
        print(line)
    if line[7] =='1' and line[8] =='b' and line[10] =='8' and line[12] == '1' and line[14]=='c' and line[24]=='9' and line[23] =='0':
        print(line)
    if line[7] =='c' and line[9] =='d' and line[11] =='1' and line[13] == '5' and line[14]=='3' and line[17] =='6' and line[18]=='6':
        print(line)
    if line[8] =='d' and line[10] =='d' and line[12] =='0' and line[13] == '7' and line[14]=='6' and line[23] =='e':
        print(line)

f.close()
#cvctf{hashisnotguessy}