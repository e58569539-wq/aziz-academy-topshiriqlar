n = int(input())
parts = input().split()
for p in parts:
    x = int(p)
    if x % 2 == 0:
        print(x)