# N ta mahsulot
# Umumiy narxni chiqaring

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
# TODO
jami = 0
for p in products:
    jami += p['price']
print(jami)