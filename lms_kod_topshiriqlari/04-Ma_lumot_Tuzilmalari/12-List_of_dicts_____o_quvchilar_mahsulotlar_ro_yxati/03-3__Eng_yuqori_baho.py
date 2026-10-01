# N ta o‘quvchi
# Eng katta bahoni chiqaring

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
ballar = []
for o in students:
    ballar.append(o['score'])
print(max(ballar))