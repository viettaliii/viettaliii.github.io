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