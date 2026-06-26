n = int(input())

teskari = 0 

while n > 0:
    teskari = teskari * 10 + (n % 10)
    n //= 10
    
print(teskari)