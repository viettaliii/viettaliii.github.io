from z3 import *

s = Solver()
flag = [BitVec(f'flag{i}', 8) for i in range(0,43)]

for i in range(1,43):
      s.add(And(flag[i]>0, flag[i]<127))

s.add(flag[0] ==99)

s.add(flag[26] + flag[41] == 109)
s.add(flag[26] + flag[32] + flag[25] + flag[17] + flag[32] + flag[38] + flag[35] + flag[10] + flag[38] + flag[41] == 706)

s.add(flag[38] + flag[22] + flag[25] + flag[22] + flag[18] + flag[33] + flag[6] + flag[9] + flag[12] + flag[6] + flag[20] == 764)

s.add(flag[21] + flag[1] + flag[4] + flag[42] + flag[41] + flag[2] + flag[25] + flag[41] + flag[3] + flag[27] + flag[14] + flag[32] + flag[22] + flag[22] + flag[2] + flag[23] == 1395)

s.add(flag[25] + flag[8] + flag[14] + flag[32] + flag[34] + flag[15] + flag[31] + flag[26] + flag[11] + flag[35] + flag[24] == 753)

s.add(flag[2] + flag[18] + flag[8] + flag[6] == 261)

s.add(flag[9] + flag[25] + flag[32] + flag[26] + flag[11] + flag[39] + flag[30] + flag[30] + flag[13] + flag[22] == 666)

s.add(flag[15] + flag[39] + flag[22] == 300)

s.add(flag[22] + flag[33] + flag[41] + flag[36] + flag[32] + flag[24] + flag[29] + flag[8] + flag[2] + flag[9] + flag[14] + flag[33] + flag[30] + flag[26] + flag[5] == 933)

s.add(flag[37] + flag[13] + flag[34] + flag[41] + flag[21] + flag[23] + flag[6] + flag[27] + flag[33] + flag[32] + flag[35] + flag[3] + flag[9] + flag[40] + flag[19] + flag[22] == 1168)

s.add(flag[23] + flag[24] + flag[29] + flag[3] + flag[25] + flag[42] + flag[42] + flag[35] + flag[42] + flag[28] + flag[21] + flag[29] + flag[20] + flag[22] + flag[10] + flag[17] + flag[31] == 1375)

s.add(flag[36] + flag[19] + flag[26] + flag[30] + flag[39] + flag[20] + flag[31] == 409)

s.add(flag[39] + flag[3] + flag[33] + flag[17] + flag[26] + flag[12] + flag[17] + flag[29] + flag[1] + flag[28] + flag[29] == 765)

s.add(flag[21] + flag[25] + flag[19] + flag[25] + flag[26] + flag[29] + flag[39] + flag[5] + flag[14] + flag[39] + flag[28] + flag[24] == 902)

s.add(flag[5] + flag[41] == 178)

s.add(flag[28] + flag[30] + flag[26] + flag[38] + flag[24] + flag[32] + flag[15] + flag[15] + flag[15] + flag[32] + flag[27] + flag[11] + flag[13] + flag[17] + flag[34] + flag[4] + flag[32] + flag[28] + flag[2] + flag[32] == 1513)

s.add(flag[7] + flag[11] + flag[41] == 165)

s.add(flag[18] + flag[2] + flag[41] + flag[35] + flag[9] + flag[12] + flag[38] + flag[17] + flag[14] + flag[11] == 653)

s.add(flag[40] + flag[31] + flag[5] + flag[23] + flag[8] + flag[30] + flag[24] + flag[25] + flag[37] + flag[30] + flag[33] + flag[29] + flag[10] + flag[5] + flag[41] + flag[13] + flag[41] + flag[20] + flag[36] == 1266)

s.add(flag[29] + flag[39] + flag[22] + flag[39] + flag[27] + flag[25] + flag[3] + flag[33] == 711)

s.add(flag[40] + flag[2] + flag[12] + flag[10] + flag[5] + flag[16] + flag[2] + flag[10] + flag[36] + flag[22] + flag[20] + flag[26] + flag[24] + flag[41] + flag[1] + flag[20] + flag[40] == 1294)

s.add(flag[5] + flag[27] + flag[2] + flag[10] + flag[21] + flag[21] + flag[19] + flag[38] + flag[26] + flag[16] + flag[38] + flag[9] + flag[16] + flag[3] + flag[29] + flag[11] + flag[36] + flag[41] + flag[42] == 1485)

s.add(flag[31] + flag[17] == 100)

s.add(flag[23] + flag[14] + flag[6] + flag[42] + flag[36] + flag[17] + flag[24] + flag[8] + flag[1] + flag[16] + flag[7] + flag[6] + flag[16] == 945)

s.add(flag[13] + flag[1] + flag[40] + flag[23] + flag[19] + flag[33] + flag[4] + flag[1] + flag[2] + flag[37] + flag[25] + flag[26] + flag[23] + flag[34] + flag[9] + flag[5] == 1327)

s.add(flag[31] + flag[40] + flag[24] + flag[13] + flag[42] + flag[28] + flag[23] + flag[13] + flag[8] + flag[3] + flag[7] + flag[14] + flag[3] + flag[15] + flag[9] + flag[24] + 2 * flag[26] + flag[41] == 1370)

s.add(flag[22] + flag[30] + flag[3] + flag[21] + flag[31] + flag[41] == 426)

s.add(flag[11] + flag[36] + flag[19] + flag[16] + flag[8] + flag[28] + flag[20] + flag[13] + flag[12] + flag[10] + flag[22] + flag[41] + flag[4] + flag[39] + flag[4] + flag[22] + flag[17] + flag[27] == 1329)

s.add(flag[7] + flag[40] + flag[1] + flag[2] + flag[20] + flag[35] + flag[23] + flag[14] + flag[15] + flag[42] + flag[38] + flag[5] + flag[38] == 1199)

s.add(flag[20] + flag[13] + flag[11] + flag[27] + flag[12] + flag[28] + flag[29] + flag[7] + flag[35] + flag[15] + flag[5] + flag[7] + flag[13] + flag[1] + flag[28] + flag[24] + flag[7] + flag[42] + flag[4] == 1470)

s.add(flag[4] + flag[17] + flag[11] == 206)

s.add(flag[30] + flag[34] + flag[41] + flag[33] + flag[28] + flag[13] + flag[8] == 470)

s.add(flag[36] + flag[17] + flag[23] + flag[33] + flag[33] + flag[18] + flag[30] + flag[6] + flag[3] + flag[11] + flag[20] + flag[5] + flag[23] + flag[23] + flag[21] + flag[17] + flag[35] + flag[13] + flag[20] == 1302)

s.add(flag[42] + flag[6] + flag[15] + flag[32] + flag[38] + flag[10] + flag[40] + flag[28] + flag[11] + flag[35] + flag[35] == 936)

s.add(flag[6] + flag[10] + flag[5] == 234)

s.add(flag[2] + flag[35] + flag[38] + flag[40] + flag[3] + flag[19] + flag[33] + flag[41] + flag[27] + flag[4] + flag[32] + flag[34] + flag[34] == 1116)

s.add(flag[10] + flag[14] + flag[17] + flag[2] + flag[16] + flag[30] + flag[5] + flag[23] + flag[4] + flag[12] == 777)

s.add(flag[29] + flag[40] + flag[33] + flag[35] + flag[8] + flag[19] == 394)

s.add(flag[31] + flag[14] + flag[9] + flag[25] + flag[20] + flag[32] + flag[17] + flag[7] + flag[14] + flag[31] + flag[30] + flag[1] == 705)

s.add(flag[2] + flag[15] == 200)

s.add(flag[13] + flag[19] + flag[6] + flag[18] + flag[30] + flag[38] + flag[14] + flag[34] + flag[38] + flag[25] + flag[36] + flag[29] + flag[35] + flag[39] + flag[34] + flag[1] == 1198)

s.add(flag[15] + flag[37] + flag[13] + flag[14] + flag[21] == 295)

if s.check() == sat:
      sol = []
      for i in range(1,43):
            sol.append(s.model().eval(flag[i]).as_long())
      print(''.join([chr(int(c)) for c in sol]))
