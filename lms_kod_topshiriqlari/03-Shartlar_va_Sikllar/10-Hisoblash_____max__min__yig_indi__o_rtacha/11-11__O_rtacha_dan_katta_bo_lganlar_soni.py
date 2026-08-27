n = int(input())
l = list(map(int, input().split()))

avg = sum(l) / n

count = sum(1 for x in l if x > avg)

print(count)