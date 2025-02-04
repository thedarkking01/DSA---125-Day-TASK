# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        level=0
        def helper(root,level):
            if not root:
                return
            if len(ans) == level:
                ans.append(root.val)
            helper(root.right, level + 1)
            helper(root.left, level + 1)
        helper(root, level)
        return ans