n = int(input())
natija = 0

for _ in range(n):
    x = int(input())
    if x % 3 == 0:
        natija += 1
        
print(natija)