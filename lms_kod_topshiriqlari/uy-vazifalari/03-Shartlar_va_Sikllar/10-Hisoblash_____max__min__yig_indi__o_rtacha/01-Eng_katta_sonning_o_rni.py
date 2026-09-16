n = int(input())

max_qiymat = -float('inf')
max_pozitsiya = 1

for i in range(1, n + 1):
    son = int(input())
    if son > max_qiymat:
        max_qiymat = son
        max_pozitsiya = i
        
print(max_pozitsiya)