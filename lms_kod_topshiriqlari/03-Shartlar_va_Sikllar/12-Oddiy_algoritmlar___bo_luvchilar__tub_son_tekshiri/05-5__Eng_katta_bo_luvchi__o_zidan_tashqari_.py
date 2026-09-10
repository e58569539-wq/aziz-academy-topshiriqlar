n = int(input())
max_div = 0

for i in range(1, n):
    if n % i == 0:
        max_div = i
        
print(max_div)