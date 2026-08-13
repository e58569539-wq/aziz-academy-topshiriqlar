n = int(input())
for i in range(n):
    row = ""
    for j in range(n):
        if j == i or j == n - 1 - i:
            row += "*"
        else:
            row += "."
    print(row)        