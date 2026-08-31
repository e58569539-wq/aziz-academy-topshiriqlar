n = int(input())
max_qiymat = -float('inf')
max_index = 0

for i in range(1, n + 1):
    son = int(input())
    if son > max_qiymat:
        max_qiymat = son
        max_index = i
        
print(max_index)