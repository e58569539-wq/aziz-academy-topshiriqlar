import sys

def slove():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    numbers = [int(x) for x in input_data[1:]]
    
    print(sum(numbers))
    
if __name__ == '__main__':
    slove()