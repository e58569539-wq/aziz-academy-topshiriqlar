# 2 qator: A va B (int)
# Jaccard = |A∩B| / |A∪B|
# Natijani 3 xonali kasr bilan chiqaring (format: {:.3f})
# Eslatma: A va B bo‘sh bo‘lib qolishi mumkin emas (testlarda shunday).

A = set(map(int, input().split()))
B = set(map(int, input().split()))
jaccard = len(A & B) / len(A | B)
print("{:.3f}".format(jaccard))