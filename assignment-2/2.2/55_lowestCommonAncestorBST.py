class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root

p_node, q_node = TreeNode(2), TreeNode(8)
root = TreeNode(6, p_node, q_node)
result = lowestCommonAncestor(root, p_node, q_node)
print(result.val)  