class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(root):
    sorted_vals = []
    
    def inorder(node):
        if not node: return
        inorder(node.left)
        sorted_vals.append(node.val)
        inorder(node.right)
        
    def build_tree(nums):
        if not nums: return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = build_tree(nums[:mid])
        node.right = build_tree(nums[mid+1:])
        return node
        
    inorder(root)
    return build_tree(sorted_vals)

root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
balanced_root = balanceBST(root)
print(balanced_root.val)  