n = int(input())
found = False

for _ in range(n):
    x = int(input())
    if not found and x % 7 == 0:
        print(x)
        found = True
        break
        
if not found:
    print("yo'q")