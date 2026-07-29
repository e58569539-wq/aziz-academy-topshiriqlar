menu = input().strip()
n = int(input().strip())

if menu == '1':
    minut = n // 60
    soniya = n % 60
    print(f"{minut} minut {soniya} soniya")
elif menu == '2':
    soat = n // 60
    minut = n % 60
    print(f"{soat} soat {minut} minut")
else:
    print("Notogri tanlov")