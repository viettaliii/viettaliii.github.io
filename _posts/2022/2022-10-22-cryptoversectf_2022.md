---
title: Writeup Cryptoverse CTF 2022 
author: vietzettt
date:  2022-10-22 
layout: post
published: true 
---

---

##### **Nguồn ở đây nhá các bạn:** [💀**Nhấp em đi**👆](/src/2022/Cryptoversectf/)

Chào các bạn đến với một chút tâm sự của tôi sau cái giải newbie nè😁))

### 1: Baby Reverse (Solved)

![title_task_01](/src/2022/Cryptoversectf/Baby_Reverse/00_title.png)

Kiểm tra file vừa tải về và nhận flag:

![result](/src/2022/Cryptoversectf/Baby_Reverse/01_result.png)

### 2: Basic Transforms (Solved)

![title](/src/2022/Cryptoversectf/Basic_Transforms/00_title.png)

Tiếp theo thử thách này là 1 thử thách được viết bằng `js`:

```js
var readline = require('readline');
var Crypto = require('vigenere');

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

rl.on('line', function(line){
    if (line.length == 20 && line.startsWith("cvctf{") && line.endsWith("}")) {
        var cat = Crypto.encode(line.substring(6, line.length - 1), "nodejsisfun").split('').map(function(c) {
            return String.fromCharCode(c.charCodeAt(0) + 1);
        }).join('');
        if (Buffer.from(cat.split("").reverse().join("")).toString('base64') == "QUlgNGoxT2A2empxMQ==") {
            console.log("Correct!");
        }
    }
});
```

Phân tích 1 chút nào: `flag` sẽ có `length = 20` và bắt đầu theo format của giải, tiếp theo sẽ mã hóa chuỗi con ngoại trừ `cvctf{` và `}`. Nhận thấy task mã hóa substring bằng `vigenere cipher` với `key = nodejsisfun` và tách mã endcode nhận được thành mảng rồi cộng mỗi pt của mảng cho 1. Tiếp theo sẽ chuyển thành string và mã hóa base64 rồi so sánh nếu bằng `QUlgNGoxT2A2empxMQ==` là đúng flag.

Và đây lời giải của tôi:

```python
import base64
a = 'QUlgNGoxT2A2empxMQ=='
b = base64.b64decode(a).decode('utf-8')
c = b[::-1]
d= []
for i in c:
    d.append(chr(ord(i)-1))

e = ''.join(d)
print(e)

# var Crypto = require('vigenere');
# console.log(Crypto.decode("0piy5_N0i3_H@","nodejsisfun"))
# result: 0bfu5_N0d3_H@
# https://playcode.io/empty_javascript
# mở và thực hiện trên web
```

Với thử thách này tôi mất khá nhiều thời gian vì không giải mã của `vigenere cipher` nên không đúng theo nền tảng `js`.

### 3: French (Solved)

![title](/src/2022/Cryptoversectf/French/00_title.png)

Mở và check kiểu file:
![type](/src/2022/Cryptoversectf/French/01_check_type_file.png)

Đây là file chạy trên hệ điều hành mã nguồn mở linux hay ubuntu 64 bit. Tiếp theo mình mở nó trên IDA pro 64 bit xem sao nhá:

```c

int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int i; // [rsp+4h] [rbp-7Ch]
  char ptr[32]; // [rsp+10h] [rbp-70h] BYREF
  __int64 v6[2]; // [rsp+30h] [rbp-50h] BYREF
  int v7; // [rsp+40h] [rbp-40h]
  __int16 v8; // [rsp+44h] [rbp-3Ch]
  char v9; // [rsp+46h] [rbp-3Ah]
  char v10[40]; // [rsp+50h] [rbp-30h] BYREF
  unsigned __int64 v11; // [rsp+78h] [rbp-8h]

  v11 = __readfsqword(40u);
  strcpy(v10, "GEL DESINFECTANT POUR LES MAINS");
  fread(ptr, 1uLL, 0x17uLL, _bss_start);
  v6[0] = 0x5FF83441E17900E5LL;
  v6[1] = 0xDF970AF589793ADLL;
  v7 = 1229849353;
  v8 = -27939;
  v9 = -73;
  rc4_crypt((__int64)v6, 0x17uLL, (__int64)v10, 31LL);
  for ( i = 0; i <= 0x16; ++i )
  {
    if ( *((_BYTE *)v6 + (int)i) != ptr[i] )
      return 1;
  }
  puts("Correct!");
  return 0;
}
```

và `f5` thần thánh, tôi thấy một thứ hay là đoạn vòng lặp kiểm tra là chỉ kiểm tra flag mình nhập với stack là có kết quả, nên tôi sẽ đặt breakpoint tại trước vòng lặp và sau thực hiện xong hàm mã hóa đoạn `"GEL DESINFECTANT POUR LES MAINS"` thành flag. Và Debug đọc stack nhận được cái cần nhận được:

![re](/src/2022/Cryptoversectf/French/03_result.png)

### 4: World Cup Predictions (Solved)

![title](/src/2022/Cryptoversectf/World_Cup_Predictions/00_title.png)

Ý tưởng bài: bài yêu cầu dự đoán đúng theo ý của tác giả là cần nhập kết quả dự đoán đội nào sẽ nhất của mỗi bảng, nếu đoán đúng các đội nhất mỗi bảng thì sẽ đến phần tiếp theo là đoán xem ai sẽ là đội dành cup World Cup năm nay và sau đó là flag được nhận được.

![nguồn các đội](/src/2022/Cryptoversectf/World_Cup_Predictions/01_country.png)

```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  _BOOL4 v3; // edx
  _BOOL4 v4; // eax
  int v5; // edx
  _BOOL4 v6; // eax
  int v7; // edx
  _BOOL4 v8; // eax
  int v9; // edx
  _BOOL4 v10; // eax
  int v11; // edx
  _BOOL4 v12; // eax
  int v13; // edx
  _BOOL4 v14; // eax
  int v15; // edx
  _BOOL4 v16; // eax
  int v18; // [rsp+0h] [rbp-140h]
  int i; // [rsp+4h] [rbp-13Ch]
  int j; // [rsp+8h] [rbp-138h]
  char v21[33]; // [rsp+10h] [rbp-130h] BYREF
  char v22; // [rsp+31h] [rbp-10Fh]
  char v23; // [rsp+50h] [rbp-F0h]
  char v24; // [rsp+71h] [rbp-CFh]
  char v25; // [rsp+90h] [rbp-B0h]
  char v26; // [rsp+B0h] [rbp-90h]
  char v27; // [rsp+D2h] [rbp-6Eh]
  char v28; // [rsp+F0h] [rbp-50h]
  char s[40]; // [rsp+110h] [rbp-30h] BYREF
  unsigned __int64 v30; // [rsp+138h] [rbp-8h]

  v30 = __readfsqword(0x28u);
  setvbuf(stdout, 0LL, 2, 0LL);
  puts(::s);
  puts("Welcome to the World Cup Predictor!");
  puts("[+] Stage 1: Predict the first place in each group.");
  v18 = 0;                         
  for ( i = 0; i <= 7; ++i )
  {
    printf("Group %c: ", (unsigned int)(i + 65));
    fgets(&v21[32 * i], 32, stdin);
    if ( !(unsigned int)sub_12FB(&v21[32 * i]) ) //kiểm tra nếu các đội mình nhập mà không nằm trong danh sách các đội thì sẽ trừ đi 1
      --v18;
  }
  for ( j = 0; j <= 7; ++j )
  {
    if ( strlen(&v21[32 * j]) > 2 ) //check len của chuỗi mk nhập nếu lớn hơn 2 thì thỏa mãn
    {
      v3 = !j && v21[0] == 'N'; //check  ký tự đầu tiên input 1
      v4 = j == 1 && v22 == 'n'; //check  ký tự thứ 2 input 2
      v5 = v4 + v3;
      v6 = j == 2 && v23 == 'A'; //check  ký tự đầu tiên input 3
      v7 = v6 + v5;
      v8 = j == 3 && v24 == 'e'; //check  ký tự thứ 2 input 4
      v9 = v8 + v7;
      v10 = j == 4 && v25 == 'J'; //check  ký tự đầu tiên input 5
      v11 = v10 + v9;
      v12 = j == 5 && v26 == 'B'; //check  ký tự đầu tiên input 6
      v13 = v12 + v11;
      v14 = j == 6 && v27 == 'a'; //check ký tự thứ 3 của input 7
      v15 = v14 + v13;
      v16 = j == 7 && v28 == 'U'; //check  ký tự đầu tiên input 8
      v18 += v15 + v16;
    }
    else
    {
      --v18;
    }
  }
  if ( v18 > 7
    && (puts("[+] Stage 2: Predict the winner!"), fgets(s, 32, stdin), (unsigned int)sub_12FB(s))
    && strlen(s) > 2
    && s[0] == 65  // A
    && s[1] == 114  // r
    && s[2] == 103 ) //g
  {
    printf("Congrats! Here is your flag: ");
    ((void (*)(void))((char *)&sub_1288 + 1))();
    return 0LL;
  }
  else
  {
    puts("You failed.");
    return 0LL;
  }
}
```

Task 1 ta cần làm thế nào để giá trị của `v18 > 7`. Với việc kết hợp điều kiện kiểm tra để kết quả đúng nhận được 1 và toán tử `and` ta sẽ nhận được kết quả bằng 1 * 8 lần sẽ lớn hơn 7. Kết hợp với bảng này nhé:

![bảng wc](/src/2022/Cryptoversectf/World_Cup_Predictions/02_bang_wc.jpg)

Nếu như nhìn và các mà `f5` ta nhận được thì cái thì check ký tự 1 hay ký tự nào trong chuỗi, tôi thì debug để check ra kết quả còn bài này thì thử vài trường hợp cũng ra... Và tiếp theo sẽ là check ai sẽ là nhà đương kim vô địch. Quá rõ ràng với 8 kết quả và 3 kí tự đầu của đáp án. Và sau khi làm hết như trên ta nhận được flag:

![flag](/src/2022/Cryptoversectf/World_Cup_Predictions/result.png)

### 5: Super Guesser (Solved)

![title](/src/2022/Cryptoversectf/Super_Guesser/00_title.png)

Chall này được viết bằng python nên tôi ném lên mạng [PyC decompile](https://www.toolnb.com/tools-lang-en/pyc.html)

Nhận được:

```py
import hashlib, re
hashes = [
 'd.0.....f5...5.6.7.1.30.6c.d9..0',
 '1b.8.1.c........09.30.....64aa9.',
 'c.d.1.53..66.4.43bd.......59...8',
 '.d.d.076........eae.3.6.85.a2...']

def main():
    guesses = []
    for i in range(len(hashes)):
        guess = input('Guess: ')
        if not (len(guess) <= 4 or len(guess) >= 6 or re.match('^[a-z]+$', guess)): #check len(guess) == 5 và a-z
            exit('Invalid')
        if not re.match('^' + hashes[i].replace('.', '[0-9a-f]') + '$', hashlib.md5(guess.encode()).hexdigest()):
            exit('Invalid')
        guesses.append(guess)

    print(f"Flag: {guesses[0]}" + '{' + ''.join(guesses[1:]) + '}')

if __name__ == '__main__':
    main()
```

`Guess` cần nhập vào sẽ có độ dài là 5 chỉ chứa mỗi các kí tự thường từ a-z. Cần nhập 4 lần để kiểm tra. Tiếp theo kiểm tra `input` của mình đã được mã hóa bằng `md5` rồi so sánh với mảng đã cho nhưng nó được ẩn đi một phần bằng dấu chấm.

Tôi kiểm tra xem có đúng không: tôi mã hóa `cvctf` bằng `md5` thì nhận được `d70146aef5a8e5364791d3006ccd9c00` nó khớp với kết quả của đề bài.

Tôi thấy input có độ dài không quá dài chỉ 5 nên tôi tạo file nguồn với các phép thử 26*5 lần rồi mã hóa nó `md5`:

```py
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

```

Tôi nghĩ nó có cái tối ưu hơn là kiểm tra xem nó có là từ english thì viết vào file.

![nguon](/src/2022/Cryptoversectf/Super_Guesser/01_src.png)

Rồi từ đó so sánh và check ra flag:

```py
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
```

Hì là ra rồi))))🤪

### 6: Boost Game (Solved)

![title](/src/2022/Cryptoversectf/Boost_Game/00_title.png)

Với thử thách này mở bằng IDA thấy nhiều function làm rối mắt nhưng khi tôi debug thì nhận ra chỉ là chỉ kiểm tra input của mình với các số đã có sẵn thôi:////

![result](/src/2022/Cryptoversectf/Boost_Game/result.png)

và xong các thử thách RE mà tôi làm được của giải newbie này...😪

Và còn 3 chall nữa tôi không k có idea để giải, nếu có thời gian tôi sẽ nghiên cứu và viết tiếp nhé...
