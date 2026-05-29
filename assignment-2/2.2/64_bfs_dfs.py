from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start_node):
    visited = set([start_node])
    queue = deque([start_node])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def dfs(start_node):
    visited = set()
    order = []
    
    def traverse(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                traverse(neighbor)
                
    traverse(start_node)
    return order

print("BFS Order:", bfs('A')) 
print("DFS Order:", dfs('A')) 