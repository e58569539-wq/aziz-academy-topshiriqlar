n = int(input())
s = 0
count = 0

while count < n:
    x = int(input())
    count += 1
    if x <= 0:
        continue
    s += x
print(s)