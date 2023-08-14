import random

keyword = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

jumlah_password = int(input('Mau berapa banyak password yang di hasilkan?'))

for i in range(jumlah_password):
    # password = password + random.choice(keyword)
    password += random.choice(keyword)

print(password)
