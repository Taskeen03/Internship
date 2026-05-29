class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    diameter = 0
    
    def longest_path(node):
        nonlocal diameter
        if not node: return 0
        left_len = longest_path(node.left)
        right_len = longest_path(node.right)

        diameter = max(diameter, left_len + right_len)
        return max(left_len, right_len) + 1
        
    longest_path(root)
    return diameter

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(diameterOfBinaryTree(root))  