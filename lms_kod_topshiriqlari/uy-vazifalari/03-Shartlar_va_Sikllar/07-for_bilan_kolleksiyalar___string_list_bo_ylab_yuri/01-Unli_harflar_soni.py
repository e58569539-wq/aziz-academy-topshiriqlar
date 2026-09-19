soz = input().strip()

unlilar = "aeiou"

soni = 0

for ch in soz:
    if ch in unlilar:
        soni += 1
        
print(soni)