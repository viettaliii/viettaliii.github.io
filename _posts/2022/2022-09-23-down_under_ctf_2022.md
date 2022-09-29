---
title: "Writeup DownUnderCTF 2022 - RE"
author: vietzettt
date: 2022-09-23
layout: post
cover: /src/2022/DownUnderCTF/00_img_pages/cover.webp
---

---

##### **Nguồn ở đây nhá các bạn:** [💀**Nhấp em đi**👆](https://github.com/vietzettt/vietzettt.github.io/tree/main/src/2022/DownUnderCTF)

Một giải CTF lần đầu tham gia của tôi và team tôi với những kiến thức tự học sau 1 thời gian. Với nhiều challenges của nhiều mảng, nhưng tôi sẽ viết bài dưới đây là mảng của tôi yêu thích và sẽ đi theo đó là RE, một mảng rất cần cơ bản như ngôn ngữ assembly x86/x64 nhá😁

Sau đây tôi vào việc đây, nay thời tiết ở Nga như bao ngày í ì y lạnh)))🥶 à mà có lò sưởi thế là nóng lắm mn>> mà thôi gét gô🤪

### Task 1: source provided (Solved)

![Ảnh mô tả nhiệm vụ 1](/src/2022/DownUnderCTF/source-provided/img/00_title.png)

Thử thách đầu tiên là beginner thế nên tôi tin là nó sẽ không quá khó nhỉ

Tôi tải các file về và mở file `chall.S`:

```code
SECTION .data
c db 0xc4, 0xda, 0xc5, 0xdb, 0xce, 0x80, 0xf8, 0x3e, 0x82, 0xe8, 0xf7, 0x82, 0xef, 0xc0, 0xf3, 0x86, 0x89, 0xf0, 0xc7, 0xf9, 0xf7, 0x92, 0xca, 0x8c, 0xfb, 0xfc, 0xff, 0x89, 0xff, 0x93, 0xd1, 0xd7, 0x84, 0x80, 0x87, 0x9a, 0x9b, 0xd8, 0x97, 0x89, 0x94, 0xa6, 0x89, 0x9d, 0xdd, 0x94, 0x9a, 0xa7, 0xf3, 0xb2

SECTION .text

global main

main:
    xor rax, rax
    xor rdi, rdi
    mov rdx, 0x32
    sub rsp, 0x32
    mov rsp, rsi
    syscall

    mov r10, 0
l:
    movzx r11, byte [rsp + r10]
    movzx r12, byte [c + r10]
    add r11, r10
    add r11, 0x42
    xor r11, 0x42
    and r11, 0xff
    cmp r11, r12
    jne b

    add r10, 1
    cmp r10, 0x32
    jne l

    mov rax, 0x3c
    mov rdi, 0
    syscall

b:
    mov rax, 0x3c
    mov rdi, 1
    syscall

```

Đây là file được viết dưới dạng **asm x86**, do đó ta đi vào đọc xem thế nào nhé

```code
SECTION .data ; đây là mảng các số có thể để sử dụng nó để tạo thành flag
c db 0xc4, 0xda, 0xc5, 0xdb, 0xce, 0x80, 0xf8, 0x3e, 0x82, 0xe8, 0xf7, 0x82, 0xef, 0xc0, 0xf3, 0x86, 0x89, 0xf0, 0xc7, 0xf9, 0xf7, 0x92, 0xca, 0x8c, 0xfb, 0xfc, 0xff, 0x89, 0xff, 0x93, 0xd1, 0xd7, 0x84, 0x80, 0x87, 0x9a, 0x9b, 0xd8, 0x97, 0x89, 0x94, 0xa6, 0x89, 0x9d, 0xdd, 0x94, 0x9a, 0xa7, 0xf3, 0xb2

SECTION .text

global main

main:                   ; đi vào hàm nào
    xor rax, rax        ; rax = 0
    xor rdi, rdi        ; rdx = 0
    mov rdx, 0x32       ; rdx = 0x32
    sub rsp, 0x32       ; rsp = rsp - 0x32
    mov rsp, rsi
    syscall

    mov r10, 0          ; r10 = 0
l:
    movzx r11, byte [rsp + r10]    ; có lẽ cái này nó là input đầu vào
    movzx r12, byte [c + r10]      ; còn cái này .data c 
    add r11, r10                   ; input = input + r10 (khả năng add với index của nó)
    add r11, 0x42                  ; input = input + 0x42
    xor r11, 0x42                  ; input = input ^ 0x42
    and r11, 0xff                  ; input = input & 0xff
    cmp r11, r12                   ; so sánh input với từng giá trị trong .data
    jne b                          ; jump if not equal

    add r10, 1                     ; có thể hiểu ind++
    cmp r10, 0x32                  ; so sánh nó với 0x32
    jne l                          ; jump if not equal 

    mov rax, 0x3c                  
    mov rdi, 0                      ; return 0 (thỏa mãn)
    syscall

b:
    mov rax, 0x3c 
    mov rdi, 1                      ; có thể hiểu là return 1 (lỗi)
    syscall

```

Từ phân tích trên thì ta thấy rõ bài này sẽ yêu cầu ta nhập `input` flag rồi rồi mã hóa từng kí tự của `input` đem so sánh với `c`
Với bài này chỉ sử dụng toán tử `xor, and, add` nên tôi sẽ đảo ngược lại quá trình nó với `c` là đầu vào và `print` kết quả nhận được.
Và đây là source Python tôi code để tạo flag:

```code
c = [0xc4, 0xda, 0xc5, 0xdb, 0xce, 0x80, 0xf8, 0x3e, 0x82, 0xe8, 0xf7, 0x82, 0xef, 0xc0, 0xf3, 0x86, 0x89, 0xf0, 0xc7, 0xf9, 0xf7, 0x92, 0xca, 0x8c, 0xfb, 0xfc, 0xff, 0x89, 0xff, 0x93, 0xd1, 0xd7, 0x84, 0x80, 0x87, 0x9a, 0x9b, 0xd8, 0x97, 0x89, 0x94, 0xa6, 0x89, 0x9d, 0xdd, 0x94, 0x9a, 0xa7, 0xf3, 0xb2]

flag = []
for i, x in enumerate(c):
    b = ((x ^ 0x42) - 0x42 - i) % 256
    flag.append(b)
print(bytes(flag).decode())

```

Và chạy nó ta nhận được flag: `DUCTF{r3v_is_3asy_1f_y0u_can_r34d_ass3mbly_r1ght?}`
Và chúc mừng ta đã hoàn thành xong task đầu tiên nhá.

### Task 2: Legit App Not Ransomware (Solved)

### Task 3: Clicky (Solved)

### Task 4: js lock (Unsolved)

### Task 5: ezpz-rev (Unsolved)

### Task 6: xva (Unsolved)

### Task 7: click the flag (Unsolved)

### Task 8: artisan (Unsolved)
