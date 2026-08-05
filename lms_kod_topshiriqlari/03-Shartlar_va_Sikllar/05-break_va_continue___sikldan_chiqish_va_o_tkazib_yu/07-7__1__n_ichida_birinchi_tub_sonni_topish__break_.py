# n beriladi.
# 2 dan boshlab birinchi tub sonni toping.
# Topilishi bilan break qiling va o‘sha sonni chiqaring.
# Agar n < 2 bo‘lsa "No" chiqaring.
# Eslatma: tub son - 1 dan katta va faqat 1 va o‘ziga bo‘linadi.
n = int(input())
if n < 2:
    print("No")
else:
    i = 2
    while i <= n:
        prime = True
        j = 2
        while j < i:
            if i % j == 0:
                prime = False
                break
            j += 1
        if prime:
            print(i)
            break
        i += 1