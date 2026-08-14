n, m = map(int, input().split())

for i in range(n):
    row = ""
    for j in range(m):
        
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            row += "*"
        else:
            row += "."
    print(row)