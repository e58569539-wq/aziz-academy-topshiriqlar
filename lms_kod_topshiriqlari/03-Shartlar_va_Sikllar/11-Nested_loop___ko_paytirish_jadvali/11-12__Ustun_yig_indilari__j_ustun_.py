n, m = map(int, input().split())

for j in range(1, m + 1):
    ustun_yigindisi = 0
    for i in range(1, n + 1):
        ustun_yigindisi += i * j
    print(ustun_yigindisi)