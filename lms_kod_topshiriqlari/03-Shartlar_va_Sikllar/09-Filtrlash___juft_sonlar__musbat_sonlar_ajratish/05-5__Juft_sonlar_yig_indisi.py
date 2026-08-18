import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    numbers = [int(x) for x in input_data[1:]]
    
    total_sum = sum(num for num in numbers if num % 2 == 0)
    print(total_sum)
    
if __name__ == "__main__":
    solve()