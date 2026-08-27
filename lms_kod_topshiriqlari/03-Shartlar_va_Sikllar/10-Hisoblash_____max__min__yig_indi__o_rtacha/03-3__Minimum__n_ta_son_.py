n = int(input())
numbers = list(map(int, input().split()))

min_val = numbers[0]

for x in numbers:
    if x < min_val:
        min_val = x
        
print(min_val)