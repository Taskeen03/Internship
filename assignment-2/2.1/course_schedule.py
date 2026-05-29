from collections import deque

def course_schedule(n, prerequisites):

    graph = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]
    
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
        
    queue = deque([i for i in range(n) if indegree[i] == 0])
    order = []
    
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return len(order) == n

num_courses_1 = 2
prereqs_1 = [[1, 0]] 
print(course_schedule(num_courses_1, prereqs_1)) 

num_courses_2 = 2
prereqs_2 = [[1, 0], [0, 1]] 
print(course_schedule(num_courses_2, prereqs_2)) 