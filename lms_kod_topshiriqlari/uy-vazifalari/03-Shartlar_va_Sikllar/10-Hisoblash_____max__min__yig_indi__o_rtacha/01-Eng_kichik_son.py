n = int(input())

birinchi_son = int(input())
eng_kichik = birinchi_son

for _ in range(n - 1):
    son = int(input())
    if son < eng_kichik:
        eng_kichik = son
        
print(eng_kichik)