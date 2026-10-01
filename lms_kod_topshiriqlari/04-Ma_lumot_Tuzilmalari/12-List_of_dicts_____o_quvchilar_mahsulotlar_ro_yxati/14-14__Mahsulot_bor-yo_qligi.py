# N ta mahsulot
# Keyin mahsulot nomi X
# Agar bor bo‘lsa YES, bo‘lmasa NO

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
x = input().strip()
# TODO
bor = False
for p in products:
    if p['name'] == x:
        bor = True
if bor:
    print("YES")
else:
    print("NO")