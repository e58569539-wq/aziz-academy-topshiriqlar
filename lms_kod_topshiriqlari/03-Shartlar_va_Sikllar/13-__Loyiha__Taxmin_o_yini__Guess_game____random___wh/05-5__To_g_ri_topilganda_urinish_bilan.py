import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    secret = 4
    
    for index, item in enumerate(input_data, start=1):
        num = int(item)
        if num == secret:
            print(f"Correct in {index} tries")
            break
            
if __name__ == '__main__':
    solve()