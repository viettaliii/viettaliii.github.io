---
title: 🐳forkbomb.ru
author: vietzettt
date:  0000-08-02
layout: post
published: false 
cover: /src/Learn/forkbomb.ru/00_conver.png
---

---

[`https://rev-kids20.forkbomb.ru/`](https://rev-kids20.forkbomb.ru/)

##### **Nguồn ở đây nhá các bạn:** [💀**👆👆👆**💀](https://github.com/vietzettt/vietzettt.github.io/tree/main/src/Learn/forkbomb.ru)

### Keygen Me (17)

![title task 17](/src/Learn/forkbomb.ru/17/task17_title.png)

```python
email = input("What is your email: ")
serial = []
for i in email:
    temp = ord(i) | 32
    if temp >=97 and temp <=122:
        for j in range(255):
            if (j | 32) == (7* (temp - 97) % 26 + 97):
                serial.append(j)
                break
print("Here is your serial: ")
for i in serial:
    print(chr(i), end='')
```

### spbctf_4_x86_64 (20)

![title task 20](/src/Learn/forkbomb.ru/20/task20_title.png)

```py
lst1 = [8,7,5,4,1,3,2,6,9,10] # nguồn chương trình
"""
Phần tìm lst2 đó là ta chạy thử
Ý tưởng bài này là di hoán đổi giá trị trước và sau cho nhau tại các vị trí trong chuỗi lst2 cần tìm -> làm sao cho lst1 được sắp xếp theo thứ tự

lst1 = [8,7,5,4,1,3,2,6,9,10]
for i in range(100):
    j = int(input())
    temp = lst1[j]
    lst1[j] = lst1[j+1]
    lst1[j+1] = temp
    print(lst1)
"""
lst2 = [0,1,2,3,4,5,6,0,1,2,3,4,5,0,1,2,3,0,1,2,1] # input cần tìm

# kiểm tra xem có đúng không?
for i in range(len(lst2)):
    temp = lst1[lst2[i]]
    lst1[lst2[i]] = lst1[lst2[i]+1] 
    lst1[lst2[i]+1] = temp
print(lst1)

#in ra chuỗi cần tìm để ra flag:
for i in lst2:
    print(chr(i+48),end='')
# 012345601234501230121

# mã hóa str của chương trình đem xor với chuỗi tìm được là ra flag. mà thôi đưa vào nó ra luôn nhé:
#  .\spbctf_4.exe 012345601234501230121
# Your flag: SayNoToBoringProgrammingLabs
```

<!-- ### Task 3

### Task 4

### Task 5 -->
