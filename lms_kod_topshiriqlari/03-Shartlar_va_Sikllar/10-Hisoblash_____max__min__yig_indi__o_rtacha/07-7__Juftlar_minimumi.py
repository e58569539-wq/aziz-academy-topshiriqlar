input()
l = [int(x) for x in input().split() if int(x) % 2 == 0]
print(min(l) if l else "No")