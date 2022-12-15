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