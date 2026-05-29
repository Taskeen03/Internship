class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    if not root: return False
    if not root.left and not root.right:
        return targetSum == root.val
    
    remaining = targetSum - root.val
    return hasPathSum(root.left, remaining) or hasPathSum(root.right, remaining)

root = TreeNode(5, TreeNode(4), TreeNode(8))
print(hasPathSum(root, 9)) 