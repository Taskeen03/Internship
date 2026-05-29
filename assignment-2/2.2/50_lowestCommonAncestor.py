class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
        
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right

p_node = TreeNode(5)
q_node = TreeNode(1)
root = TreeNode(3, p_node, q_node)

lca = lowestCommonAncestor(root, p_node, q_node)
print(lca.val) 