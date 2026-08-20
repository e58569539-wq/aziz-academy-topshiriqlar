n = int(input())
sonlar = list(map(int, input().split()))

hisob = 0
for x in sonlar:
    if x % 3 == 0:
        hisob += 1
        
print(hisob)