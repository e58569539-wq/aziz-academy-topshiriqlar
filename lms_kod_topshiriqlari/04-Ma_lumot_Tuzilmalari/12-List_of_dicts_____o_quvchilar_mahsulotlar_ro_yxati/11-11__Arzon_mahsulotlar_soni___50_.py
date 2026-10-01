# N ta mahsulot
# Narxi 50 dan kichik bo‘lganlar sonini chiqaring

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
# TODO
soni = 0
for p in products:
    if p['price'] < 50:
        soni += 1
print(soni)