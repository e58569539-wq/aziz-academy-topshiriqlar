# n = int(input())
# skip = int(input())
# while i<=n, agar i==skip bo'lsa continue qiling.
n = int(input())
skip = int(input())
i = 0
while i < n:
    i += 1
    if i == skip:
        continue
    print(i)