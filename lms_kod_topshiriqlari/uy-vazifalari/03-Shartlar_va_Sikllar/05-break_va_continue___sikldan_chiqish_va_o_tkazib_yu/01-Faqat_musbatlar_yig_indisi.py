n = int(input())
yigindi = 0

while n > 0:
    son = int(input())
    if son <= 0:
        n -= 1
        continue
    yigindi += son
    n -= 1
    
print(yigindi)