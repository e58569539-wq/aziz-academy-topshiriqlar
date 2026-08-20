import sys

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    
    toq_yigindi = 0
    for i in range(1, n + 1):
        son = int(data[i])
        if son% 2 != 0:
            toq_yigindi += son
            
    print(toq_yigindi)