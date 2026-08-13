n = int(input())

for i in range(1, n + 1):
    
    yulduz = "*" * (2 * i - 1)
    
    bosh_joy = " " * (n - i)
    
    print(bosh_joy + yulduz)