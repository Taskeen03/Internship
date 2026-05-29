import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

nums_input = [1, 1, 1, 2, 2, 3]
k_input = 2
result = topKFrequent(nums_input, k_input)
print(result) 