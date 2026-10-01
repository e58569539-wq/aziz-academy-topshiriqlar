# 2 qator: A va B
# Intersection (A ∩ B) ni toping.
# Agar kesishma bo‘sh bo‘lsa: BO'SH chiqaring
# Aks holda: SORT qilingan elementlar space bilan

a = set(map(int, input().split()))
b = set(map(int, input().split()))
kesishma = a & b
if kesishma:
    print(" ".join(str(x) for x in sorted(kesishma)))
else:
    print("BO'SH")