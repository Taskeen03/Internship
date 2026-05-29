class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMinMax(root):
    if not root: return float('inf'), float('-inf')
    
    left_min, left_max = findMinMax(root.left)
    right_min, right_max = findMinMax(root.right)
    
    current_min = min(root.val, left_min, right_min)
    current_max = max(root.val, left_max, right_max)
    
    return current_min, current_max

root = TreeNode(4, TreeNode(2, TreeNode(1)), TreeNode(7))
tree_min, tree_max = findMinMax(root)
print(f"Min: {tree_min}, Max: {tree_max}")  