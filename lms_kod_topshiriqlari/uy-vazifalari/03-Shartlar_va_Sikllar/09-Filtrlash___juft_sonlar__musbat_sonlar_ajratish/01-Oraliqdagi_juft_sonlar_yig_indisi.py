a = int(input())
b = int(input())

yigindi = sum(i for i in range(a, b + 1) if i % 2 == 0)
print(yigindi)