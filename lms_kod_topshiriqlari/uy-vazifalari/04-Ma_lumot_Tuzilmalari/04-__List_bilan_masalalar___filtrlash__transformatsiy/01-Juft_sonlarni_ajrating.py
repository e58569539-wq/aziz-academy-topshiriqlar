sonlar = map(int, input().split())
juftlar = [str(x) for x in sonlar if x % 2 == 0]
print(" ".join(juftlar))