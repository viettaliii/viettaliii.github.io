---
title: M*CTF Trainning 2023
author: vietzettt
date:  2023-02-26
layout: post
published: true
cover: /src/2023/MCTFtrainning2023/cover.svg
---

---

##### **Nguồn ở đây nhá các bạn:** [💀**👆👆👆**💀](https://github.com/vietzettt/vietzettt.github.io/tree/main/src/MCTFtrainning2023)

Xin chào tất cả mọi người đến với giải đấu team tôi xung mãn lực lượng í ì i.... Rất nhiều mảng nhiều challs để giải rất phù hợp cho mấy người mới chơi CTF (vì nó là đào tạo để thi đấu).

Sau đây tôi sẽ viết 3 bài reverse của giải, nó khá dễ nhưng lại (nhưng 2 challs sau nó k hay và hơi đụn tí).

### 1: Tango

![title](/src/2023/MCTFtrainning2023/tango/00_title.png)

Đối với cái bài này thì họ cho ta file viết bằng python -> mở nó ra và cùng đọc nhé

```py

from random import randrange as rr, seed

seed(0XDEAD_0060)

FLAG = '-------------- REMOVED --------------'
FLAG = bytearray(FLAG, 'utf-8')

for _ in range(len(FLAG)):
    FLAG[_] &= (((rr(2) << 16) + 0xDEAD + (0X_49_4E_53_49_44_45 >> 50)) >> 16) + (- (1 << 0O7 - 0B10) + (1 << 0B111) | 0B1110100) ^ ((0B10101111 << 0 | (0X1 << 0O2) + (0O1 << 0B11)) & 0B10011010 >> 0)

print('Encrypted flag:', FLAG.decode())
```

Như đọc trên thì ta thấy `FLAG` đã bị xóa và mình cần tìm nó để chạy chương trình ra flag thỏa mãn với kết quả của yêu cầu chall mà giải đưa ra là `lbtf{ly^4l8o^0r_r3ctr3^6r0ll^d3sp41r}`.

Cùng nhìn vào đoạn mã trên và phân tích nhé.

Chương trình có vòng lặp duyệt từng phần tử trong `FLAG` mỗi phần tử này sẽ được AND với 1 biểu thức kia chưa 1 giá trị nào đó mà tôi không quan tâm về nó.

Nếu quan tâm về nó thì cũng đơn giản thôi: hàm `rr` viết tắt của `randrange` như đã định nghĩa ở dòng đầu. Hàm này sẽ lấy giá trị ngẫu nhiên trong khoảng xác định. Như trên thì sẽ có giá trị có thể nhận là 0 hoặc 1. Nhưng có thêm hàm `seed()` thì giá trị này sẽ được cố định theo giá trị seed -> ta nhận được giá trị 0.

Tiếp đến là các số thuộc hệ 2,8,10,16 thôi không có gì cả, cái đó thì để máy tính nó tính cho)). Kết quả của cả cái dài nó là 254.

Đó thế thôi có thể ta dùng vòng lặp thử giá trị bất kỳ trong bảng mã accsii nếu giá trị đó & với 254 mà bằng với giá trị của flag họ cho là được.

1 Lưu ý vì nó là toán tử bit & thế nên sẽ nhận là giá trị chính nó và giá trị khác khi có thể.

Như thường lệ thì tôi sử dụng z3 để làm nó cho nó đơn giản máy móc để phục vụ mình. Dưới đây là code của tui.

```py
from random import randrange as rr, seed
from z3 import *
seed(0XDEAD_0060)
s = Solver()

flag = [BitVec(f'flag{i}', 8) for i in range(0, 37)] # tạo mảng flag
result = 'lbtf{ly^4l8o^0r_r3ctr3^6r0ll^d3sp41r}'

for i in range(37):
    s.add(flag[i] & ((((rr(2) << 16) + 0xDEAD + (0x494E53494445 >> 50)) >> 16) + (- (1 << 7 - 2) +
          (1 << 7) | 116) ^ ((175 << 0 | (1 << 2) + (1 << 3)) & 154 >> 0)) == ord(result[i])) # add các điều kiện cho z3 kiểm tra
    
    if i in [0, 1, 7, 5, 10, 12, 13, 14, 16, 19, 22, 23, 28]: # cái này là mò từng trường hợp lười làm cách khác
        s.add(Not(flag[i] == ord(result[i])))


if s.check() == sat: # kiểm tra và in ra flag..
    sol = []
    for i in range(37):
        sol.append(s.model().eval(flag[i]).as_long())
    print(''.join([chr(int(c)) for c in sol]))

```

Có cách khác không dùng z3 là ta dùng vòng lặp thử giá trị ... như tôi đã đề cập ở trên. Ví dụ như sau:

```py
>>> for i in range(127):
...     if i & 254 == ord('l'):
...             print(chr(i))
...
l
m
```

Như ký tự đầu tiên là có 2 kết quả ký tự `l` và `m` thỏa mãn -> do đó ta sẽ chạy vòng lặp đến tất cả các phần tử của flag. Rồi ta ghép các trường hợp xảy ra xem trường hợp nào flag có nghĩa là đúng.

Dưới đây là cách bằng for đơn giản hơn. Tôi tạo ra 1 list các quả có thể nhận được. Vì nó có nghĩa cũng k dài, thế nên sau khi nhận được list đó ta thử ghép vào nhìn mấy khả năng là ra flag.

```py
result = 'lbtf{ly^4l8o^0r_r3ctr3^6r0ll^d3sp41r}'
lst = []
for j in result:
    temp = []
    for i in range(127):
        if i & 254 == ord(j):
            temp.append(chr(i))
    if len(temp) == 0:
        temp.append(j)
    lst.append(temp)
```

Từ list ta ghép lại mấy khả năng ta nhận được flag có nghĩa: ... `mctf{my_4l9o_1s_s3cus3_7r0ll_d3sp41r}` - `my_algo_secuse_troll_despair`.

Thế là xong nhé.

### 2: 16 bit

![title](/src/2023/MCTFtrainning2023/16_bit/00_title.png)

Tiếp đến là bài này. Bài này hơi xàm 1 là chạy chương trình thì thỏa mãn rất nhiều key là đều đúng. Thế nên tôi đi hỏi người ra đề, thì đề đó có nhiều cách giải nhưng flag gửi là phải theo đúng kết quả của người ra đề... (thật khó để ra)

Mở IDA lên ra đọc:

![flow](/src/2023/MCTFtrainning2023/16_bit/01_flow_check.png)

Đó như thấy thì quan trọng của chương trình này là 2 cái so sánh chính của key.

Kiểm tra kích thước của key với `10h` tương đương với 16 ký tự, và `sum` của tất cả các ký tự trong key == 1762. Là nhận được `YEAP....`

Bởi lẽ đó mà tôi ngồi cắm đầu vào làm z3 rồi kiếm xem flag nào có nghĩa nhưng không thật khó để tìm được vì không gian mẫu của nó rất lớn...

Vì rõ ràng là ta mà chạy được thì kết quả nó sẽ đúng. Nhưng flag gửi không chấp nhận vì kết quả so sánh khi nhập là 1 trong cái không gian mẫu to bự kia...

Thế thì chịu... Tôi đi hỏi người ra đề thì người ta bảo là lấy giá trị 1762/16 là ra 15 ký tự ban đầu còn lại sẽ là ký tự cuối cùng. Thật hay :)...

Thôi cũng không có gì để nói với cái bài này. Flag: `MCTF{nnnnnnnnnnnnnnnp}`.

### 3: Incorrect password

![title](/src/2023/MCTFtrainning2023/Incorrect_password/00_title.png)

Và cái bài này ối dồi ôi hệ thống khả năng lỗi vì lúc đầu tôi gửi đúng là chắc do họ để flag sai nên gửi không chấp nhận. Thế là tôi đi mò tung các ngoại lệ của chương trình đấy ra... rồi cũng không có gì...

Thế là tôi đi gửi lại flag thì nó được:00))) thật là 🥲

Đây là flow của chương trình:

![flow](/src/2023/MCTFtrainning2023/Incorrect_password/01_flow.png)

Đọc 1 tí là thấy hàm kiểm tra thông qua chuỗi `password1`, mỗi phần tử đều trừ đi 1 rồi in ra key :))

Bạn thấy dòng `dec edx` không chính nó đấy. Rồi nó đem `edx` so sánh với `ecx` (thanh ghi chứa input của mình).

và xong không có gì cả :). Flag: ``MCTF{o`rrvnqc0}``

Cảm ơn các bạn đã theo dõi đến đây. Vì nó là giành cho người mới bắt đầu thế nên tôi cũng không học được gì nhiều từ giải này...
