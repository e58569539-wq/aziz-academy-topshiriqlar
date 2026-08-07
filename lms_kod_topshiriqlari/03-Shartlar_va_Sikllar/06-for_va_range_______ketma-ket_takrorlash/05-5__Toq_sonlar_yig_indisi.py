# n beriladi.
# 1..n oralig‘idagi toq sonlar yig‘indisini for bilan top.
n = int(input())
yigindi = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        yigindi += i
print(yigindi)