class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node: return None
    
    old_to_new = {}
    
    def dfs(curr_node):
        if curr_node in old_to_new:
            return old_to_new[curr_node]

        copy = Node(curr_node.val)
        old_to_new[curr_node] = copy
        
        for neighbor in curr_node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    return dfs(node)

node1 = Node(1)
node2 = Node(2)
node1.neighbors.append(node2)
node2.neighbors.append(node1)

cloned_head = cloneGraph(node1)
print(cloned_head.val)                  
print(cloned_head.neighbors[0].val)    