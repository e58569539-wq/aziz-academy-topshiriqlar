# 2 qator: A va B
# A - B ni toping.
# Agar bo‘sh bo‘lsa: BO'SH
# Aks holda: SORT qilingan elementlar space bilan

a = set(map(int, input().split()))
b = set(map(int, input().split()))
farq = a - b
if farq:
    print(" ".join(str(x) for x in sorted(farq)))
else:
    print("BO'SH")