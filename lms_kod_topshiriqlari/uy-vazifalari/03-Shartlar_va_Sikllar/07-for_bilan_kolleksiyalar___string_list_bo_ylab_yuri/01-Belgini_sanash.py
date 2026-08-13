char = input()
word = input()

count = 0
for ch in word:
    if ch == char:
        count += 1
        
print(count)