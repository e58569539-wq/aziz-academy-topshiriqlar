from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

counts = Counter(numbers)

max_freq = max(counts.values())

most_common_elements = [num for num, freq in counts.items() if freq == max_freq]

print(min(most_common_elements))