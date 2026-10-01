# N ta mahsulot
# Eng arzon mahsulot nomini chiqaring

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
# TODO
eng = products[0]
for p in products:
    if p['price'] < eng['price']:
        eng = p
print(eng['name'])