n = int(input())
soni = 0

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        if i * i == n:
            soni += 1
        else:
            soni += 2
            
print(soni)