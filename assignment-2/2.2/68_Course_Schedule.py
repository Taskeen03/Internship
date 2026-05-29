def canFinish(numCourses, prerequisites):
    adj = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses
    
    for course, pre in prerequisites:
        adj[pre].append(course)
        indegree[course] += 1
        
    from collections import deque
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    visited_count = 0
    
    while queue:
        node = queue.popleft()
        visited_count += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return visited_count == numCourses

num_courses = 2
prereqs = [[1, 0]] 
result = canFinish(num_courses, prereqs)
print(result) 