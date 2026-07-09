gap = input()

tozalangan_boshliq = gap.replace(",", " ")

sozlar_royxati = tozalangan_boshliq.split()

chiroyli_gap = " ".join(sozlar_royxati)

sozlar_soni = len(sozlar_royxati)

print(chiroyli_gap)
print(sozlar_soni)