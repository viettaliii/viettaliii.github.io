import base64

d = "UkZWRFZF"
u = "WjdaREZrWDNrd2RW"
c = "OXdZV"
t = "zR4WTE4d2NsOWpNREJzWDJG"
f = "elgyTjFZM1Z0WWpOeWZRPT0"

en_flag = ""
en_flag =en_flag+ d + u + c+ t+f+'='
flag = base64.b64decode(en_flag).decode()

print(flag)