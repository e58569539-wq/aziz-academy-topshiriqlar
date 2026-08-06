# n beriladi.
# 1..n ichida birinchi 4 ga karrali sonni top.
# Topilsa o‘sha sonni chiqarib break.
# Topilmasa "No" chiqar.
n = int(input())
i = 1
found = False
while i <= n:
    if i % 4 == 0:
        print(i)
        found = True
        break
    i += 1
if not found:
    print("No")