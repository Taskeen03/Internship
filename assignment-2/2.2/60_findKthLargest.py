import heapq

def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
            
    return heap[0]

nums_input = [3, 2, 1, 5, 6, 4]
k_input = 2
result = findKthLargest(nums_input, k_input)
print(result)  