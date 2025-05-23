# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced=left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]


# Using bottom-up recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            if abs(left_height - right_height) > 1:
                self.balanced = False
            return 1 +max(left_height,right_height)

        height(root)
        return self.balanced
