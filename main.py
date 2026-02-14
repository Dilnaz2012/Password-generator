import random

password =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
q = int(input("Напишите длину пароля"))
a = ""
for i in range(q):
    a += random.choice(password)
print(a)
