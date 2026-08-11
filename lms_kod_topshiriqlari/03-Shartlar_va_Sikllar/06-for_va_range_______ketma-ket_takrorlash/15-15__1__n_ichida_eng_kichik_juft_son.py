n = int(input())
topildi = False
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
        topildi = True
        break
if not topildi:
    print("No")