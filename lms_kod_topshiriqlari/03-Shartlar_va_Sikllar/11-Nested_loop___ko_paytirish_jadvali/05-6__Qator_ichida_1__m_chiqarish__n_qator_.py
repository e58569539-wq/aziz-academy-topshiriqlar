data = list(map(int, input().split()))

if len(data) == 1:
    print(data[0])
else:
    n, m = data
    for _ in range(n):
        print(*range(1, m + 1))