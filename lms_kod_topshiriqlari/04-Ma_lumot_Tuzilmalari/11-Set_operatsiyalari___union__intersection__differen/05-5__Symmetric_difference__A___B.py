# 2 qator: A va B
# A ^ B (faqat bittasida borlar) ni toping.
# Agar bo‘sh bo‘lsa: BO'SH
# Aks holda: SORT qilingan elementlar space bilan

a = set(map(int, input().split()))
b = set(map(int, input().split()))
simmetrik = a ^ b
if simmetrik:
    print(" ".join(str(x) for x in sorted(simmetrik)))
else:
    print("BO'SH")