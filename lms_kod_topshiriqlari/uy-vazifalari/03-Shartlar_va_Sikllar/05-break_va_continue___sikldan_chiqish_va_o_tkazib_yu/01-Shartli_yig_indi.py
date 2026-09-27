total = 0

while True:
    x = int(input())
    
    if x == 0:
        break
    elif x < 0:
        continue
    elif x > 100:
        break
        
    total += x
    
print(total)