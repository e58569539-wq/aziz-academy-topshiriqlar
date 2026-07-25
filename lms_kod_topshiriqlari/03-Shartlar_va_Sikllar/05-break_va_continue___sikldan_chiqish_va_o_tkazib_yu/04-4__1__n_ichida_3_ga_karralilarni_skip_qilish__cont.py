# n beriladi.
# 1..n oralig‘ida 3 ga karrali sonlarni chiqarma (continue).
# Qolgan sonlarni har qatorda bitta chiqar.
n = int(input())
i = 0 
while i < n:
    i += 1
    if i % 3 == 0:
        continue
    print(i)