n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        kopaytma = i * j
        if kopaytma % 2 == 0:
            print(f"{i} x {j} = {kopaytma}")