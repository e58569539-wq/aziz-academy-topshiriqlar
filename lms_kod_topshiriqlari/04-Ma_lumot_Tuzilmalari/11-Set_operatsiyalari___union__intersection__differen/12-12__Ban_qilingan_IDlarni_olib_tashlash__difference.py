# 3 qator:
# 1-qator: IDlar (int)
# 2-qator: ban qilingan IDlar (int)
# 3-qator: (bo‘sh bo‘lishi mumkin) — e'tibor bermang (faqat ko‘p test uchun)
# Ruxsat etilgan = IDlar - banned
# Natija: SORT qilingan IDlar space bilan. Agar bo‘sh bo‘lsa: BO'SH

ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()
ruxsat = ids - banned
if ruxsat:
    print(" ".join(str(x) for x in sorted(ruxsat)))
else:
    print("BO'SH")