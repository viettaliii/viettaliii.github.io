#nhận kết quả từ trên nc ....
flag_encode = "af a5 a8 ae b2 a5 a0 a7 bc b1 96 ba a1 a6 bc a5 ad 96 a8 ad ad 96 a4 b0 96 a4 ac a4 af bb a6 ab b4"

lst_from_flag = flag_encode.split(" ") # tách và chuyển thành list

lst_int_fe = []
for i in lst_from_flag:
    lst_int_fe.append(int(i,16))

# [175, 165, 168, 174, 178, 165, 160, 167, 188, 177, 150, 186, 161, 166, 188, 165, 173, 150, 168, 173, 173, 150, 164, 176, 150, 164, 172, 164, 175, 187, 166, 171, 180]

v7 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144][::-1] # list các số xor nên ngược lại là ...

for i in lst_int_fe:
    for j in v7:
        i = i ^ j
    print( chr(i) ,end='')


