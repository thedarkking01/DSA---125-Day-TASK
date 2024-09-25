# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left)+[root.val]+inorder(root.right)
        
        def balancedTree(nums):
            if not nums:
                return None
            mid=len(nums)//2
            root=TreeNode(nums[mid])
            root.left=balancedTree(nums[:mid])
            root.right=balancedTree(nums[mid+1:])
            return root
        sortednode=inorder(root)
        return balancedTree(sortednode)