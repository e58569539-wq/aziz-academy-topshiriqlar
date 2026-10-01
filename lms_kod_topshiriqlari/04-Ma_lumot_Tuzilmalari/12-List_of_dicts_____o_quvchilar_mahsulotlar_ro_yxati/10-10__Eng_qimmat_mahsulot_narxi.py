# N ta mahsulot
# Eng qimmat mahsulot narxini chiqaring

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
# TODO
narxlar = []
for p in products:
    narxlar.append(p['price'])
print(max(narxlar))