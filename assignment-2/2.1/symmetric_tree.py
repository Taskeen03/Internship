class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def are_symmetric(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2 or root1.val != root2.val:
        return False
    return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)

def is_symmetric(root):
    return True if not root else are_symmetric(root.left, root.right)

tree = TreeNode(1, TreeNode(2), TreeNode(2))
print(is_symmetric(tree))  