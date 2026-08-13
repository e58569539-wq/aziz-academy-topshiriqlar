# s beriladi.
# for bilan s ichidagi raqam (0-9) belgilar sonini chiqaring.
s = input()
c = 0
for ch in s:
    if ch.isdigit():
        c += 1
print(c)