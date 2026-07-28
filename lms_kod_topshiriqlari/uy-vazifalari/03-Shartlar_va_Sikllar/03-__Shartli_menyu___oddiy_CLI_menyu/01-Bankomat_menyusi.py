action = int(input())
balance = int(input())
amount = int(input())

if action == 1:
    print(balance)
elif action == 2:
    if amount <= balance:
        print(balance - amount)
    else:
        print("Mablag' yetarli emas")
elif action == 3:
    print(balance + amount)
else:
    print("Notogri amal")