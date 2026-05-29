import heapq

def kClosest(points, k):
    heap = []
    
    for x, y in points:
        dist = -(x**2 + y**2)
        if len(heap) < k:
            heapq.heappush(heap, (dist, [x, y]))
        else:
            if dist > heap[0][0]:
                heapq.heapreplace(heap, (dist, [x, y]))
                
    return [pair[1] for pair in heap]

points_input = [[1, 3], [-2, 2]]
k_input = 1
result = kClosest(points_input, k_input)
print(result)  