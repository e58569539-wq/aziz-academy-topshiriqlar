import sys
data = list(map(int, sys.stdin.read().split()))
print(sum(1 for x in data[1:] if x % 3 == 0))