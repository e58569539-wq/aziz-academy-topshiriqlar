# 2 qator: 2 ta gap (matn)
# Har bir gapni split() qiling, so‘zlar unionini oling.
# Natija: unikal so‘zlar sonini chiqaring.
# Eslatma: katta-kichik farq qilmasin -> lower() ishlating.

s1 = input().strip().lower().split()
s2 = input().strip().lower().split()
print(len(set(s1) | set(s2)))