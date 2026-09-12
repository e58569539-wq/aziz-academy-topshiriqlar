import sys

yashirin_son = 42

for qatator in sys.stdin:
    son = int(qatator.strip())
    if son > yashirin_son:
        print("High")
    elif son < yashirin_son:
        print("Low")
    else:
        print("Correct")
        break