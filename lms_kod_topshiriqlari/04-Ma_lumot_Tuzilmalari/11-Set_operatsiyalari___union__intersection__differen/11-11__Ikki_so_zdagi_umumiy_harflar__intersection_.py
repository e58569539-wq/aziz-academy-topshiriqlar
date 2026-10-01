# 2 qator: 2 ta string
# Umumiy harflarni toping (set intersection).
# Natija: harflarni SORT qilib bitta qatorda chiqaring.
# Agar bo‘sh bo‘lsa: BO'SH

a = input().strip()
b = input().strip()
Umumiy = set(a) & set(b)
if Umumiy:
    print("".join(sorted(Umumiy)))
else:
    print("BO'SH")