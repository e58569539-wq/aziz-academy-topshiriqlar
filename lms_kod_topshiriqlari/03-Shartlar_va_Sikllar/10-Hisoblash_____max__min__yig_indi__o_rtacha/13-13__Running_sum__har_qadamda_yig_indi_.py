n = int(input())
arr = list(map(int, input().split()))

current_sum = 0
for x in arr:
    current_sum += x
    print(current_sum)