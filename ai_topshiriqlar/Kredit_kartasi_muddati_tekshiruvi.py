# Kredit kartasi muddati tekshiruvi
# Kurs: IT Dasturlash
# Mavzu: Solishtirish operatorlari: ==, !=, >, <, >=, <=
# Ball: 100
# Aziz Academy — AI Topshiriq

sana1, sana2 = input().split()

d1, m1, y1 = map(int, sana1.split('/'))
d2, m2, y2 = map(int, sana2.split('/'))

if (y2, m2, d2) >= (y1, m1, d1):
    print("Kartangiz amal qiladi")
else:
    print("Kartangiz amal qilmaydi")