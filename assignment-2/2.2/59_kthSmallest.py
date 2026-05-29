class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    res = []
    
    def inorder(node):
        if not node or len(res) >= k: return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
        
    inorder(root)
    return res[k - 1]

root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kthSmallest(root, 2))  