n = int(input())
numbers = list(map(int, input().split()))

total = sum(x for x in numbers if x % 2 == 0)
print(total)