n = int(input())
parts = input().split()
lst = []
for p in parts:
    lst.append(int(p))
x = int(input())
idx = -1
for i in range (len(lst)):
    if lst[i] == x:
        idx = i
        break
print(idx)