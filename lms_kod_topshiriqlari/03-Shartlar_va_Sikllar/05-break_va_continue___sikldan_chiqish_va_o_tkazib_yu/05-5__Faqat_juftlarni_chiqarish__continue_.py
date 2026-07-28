# n beriladi.
# 1..n oralig‘ida faqat juft sonlarni chiqar.
# Toq bo‘lsa continue ishlat.
n = int(input())

for i in range(1, n + 1):
    if i % 2 != 0:
        continue
    print(i)