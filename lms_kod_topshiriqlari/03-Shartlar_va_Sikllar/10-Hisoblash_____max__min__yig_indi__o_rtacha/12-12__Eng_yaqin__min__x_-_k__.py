# n va n ta son beriladi, keyin k beriladi.
# k ga eng yaqin sonni topib chiqaring.
# Agar masofa teng bo‘lsa, kichikroq sonni tanlang.
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

closest = min(arr, key=lambda x: (abs(x - k), x))
print(closest)