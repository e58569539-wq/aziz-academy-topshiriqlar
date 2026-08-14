n = int(input())

if n == 1:
    print('*')
else:
    print('*' * n) 
    for _ in range(n - 2):
        print('*' + ' ' * (n - 2) + '*')
    print('*' * n)