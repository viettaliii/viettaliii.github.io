a = "oz]{R]3l]]B#50es6O4tL23Etr3c10_F4TD2" #đoạn này yêu cầu ta tách thành 3 strings gồm 6pt
a1 = a[:12]
a2 = a[12:24]
a3 = a[24:]

def re_code(a1,n): # hàm decode
    b1 = [0]*12
    n1 = 5
    n2 = 6
    for i in range(0,12,2):
        b1[n1] = a1[i]
        b1[n2] = a1[i+1]
        n1-=1
        n2+=1
    str_tem = ''
    for i in b1:
        str_tem += chr(ord(i)^n)
    return str_tem

c1 = re_code(a1,2) #sau quá trình encode
c2 = re_code(a2,1)
c3 = re_code(a3,0)

row0 = c1[:6]
row1 = c2[:6]
row2 = c3[:6]
row3 = c3[6:][::-1] #đảo ngược 6pt tiếp theo của các đoạn chuỗi đã nhập
row4 = c2[6:][::-1]
row5 = c1[6:][::-1]

# @_1P_m
# 2M57d4
# D4_13t
# 2TF0cr
# D3uNr1
# !_n_yx

matrix = []
# tạo matrix 2 chiều
matrix.append(list(row0))
matrix.append(list(row1))
matrix.append(list(row2))
matrix.append(list(row3))
matrix.append(list(row4))
matrix.append(list(row5))

# dịch ngược lại hàm solve
for i in range(0,3): # 0 ->3
    for j in range(0,6-2*i -1): # 
        c = matrix[6 - 1 - i - j][i]
        matrix[6 - 1 - i - j][i] = matrix[i][i + j]
        matrix[i][i + j] = matrix[i + j][6 - 1 - i]
        matrix[i + j][6 - 1 - i] = matrix[6 - 1 - i][6 - 1 - i - j]
        matrix[6 - 1 - i][6 - 1 - i - j] = c

print("SEKAI{",end='')
for i in matrix:
    print(''.join(i), end='') #print flag
print("}")