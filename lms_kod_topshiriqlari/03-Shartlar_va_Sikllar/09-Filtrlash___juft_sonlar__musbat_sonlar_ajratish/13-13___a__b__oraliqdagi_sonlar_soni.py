n = int(input())
sonlar = list(map(int, input().split()))
a, b = map(int, input().split())

hisob = 0
for x in sonlar:
    if a <= x <= b:
        hisob += 1
        
print(hisob)