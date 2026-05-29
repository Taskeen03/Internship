import heapq

def kth_largest(arr, k):
    if k <= 0 or k > len(arr):
        return None
        
    max_heap = [-elem for elem in arr]
    heapq.heapify(max_heap)
    
    for _ in range(k - 1):
        heapq.heappop(max_heap)
        
    return -heapq.heappop(max_heap)

numbers = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

result = kth_largest(numbers, k)
print(f"The {k}th largest element is: {result}") 