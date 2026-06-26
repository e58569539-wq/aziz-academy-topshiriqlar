summa = 0 
count = 0 

n = int(input())

while n != 0:
    summa += n 
    count += 1 
    n = int(input())
    
if count == 0:
    print(0)
else:
    print(summa / count)