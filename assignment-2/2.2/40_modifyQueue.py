from collections import deque

def modifyQueue(q, k):
    if len(q) == 0 or k > len(q) or k <= 0:
        return q
        
    stack = []
    
    for _ in range(k):
        stack.append(q.popleft())
        
    while stack:
        q.append(stack.pop())
    for _ in range(len(q) - k):
        q.append(q.popleft())     
    return q

queue_input = deque([1, 2, 3, 4, 5])
k_val = 3

result = modifyQueue(queue_input, k_val)
print(list(result))  