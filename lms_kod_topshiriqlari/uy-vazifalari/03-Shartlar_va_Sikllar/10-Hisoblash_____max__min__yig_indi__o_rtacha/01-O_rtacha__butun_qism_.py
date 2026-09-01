import sys
d = list(map(int, sys.stdin.read().split()))
print(sum(d[1:]) // d[0] if d else 0)