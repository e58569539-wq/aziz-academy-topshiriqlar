# N ta o‘quvchi
# Eng katta bahoga ega o‘quvchi nomini chiqaring

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
eng = students[0]
for o in students:
    if o['score'] > eng['score']:
        eng = o
print(eng['name'])