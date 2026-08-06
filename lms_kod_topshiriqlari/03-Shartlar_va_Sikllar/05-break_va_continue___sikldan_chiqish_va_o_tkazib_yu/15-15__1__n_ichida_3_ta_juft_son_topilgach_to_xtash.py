n = int(input())
i = 1
c = 0
found = False
while i <= n:
    if i % 2 == 0:
        c += 1
        if c == 3:
            print(i)
            found = True
            break
    i += 1
if not found:
    print("No")