class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root: return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

root = TreeNode(4, TreeNode(2), TreeNode(7))

inverted = invertTree(root)
print(inverted.left.val, inverted.right.val)  