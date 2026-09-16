matn = input()
soz = input()

yangilangan_matn = matn.replace(soz, soz.upper())
soni = matn.count(soz)

print(yangilangan_matn)
print(soni)