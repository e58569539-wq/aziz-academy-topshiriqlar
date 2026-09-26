n = int(input())
boluchilar = []

for i in range(1, n + 1):
    if n % i == 0:
        boluchilar.append(str(i))
        
print(" ".join(boluchilar))