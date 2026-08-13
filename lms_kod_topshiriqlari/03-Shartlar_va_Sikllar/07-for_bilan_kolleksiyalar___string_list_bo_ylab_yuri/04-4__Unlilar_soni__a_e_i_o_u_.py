# s beriladi.
# for bilan unlilar (a,e,i,o,u) sonini hisoblang.
# (Faqat kichik harflar deb oling.)
s = input()
c = 0
for ch in s:
    if ch in "aeiou":
        c += 1
print(c)