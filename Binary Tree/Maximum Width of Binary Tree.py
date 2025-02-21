# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        q=deque([[root,1,0]]) # [node,num,level]
        prelevel,prenum=0,1
        while q:
            node,num,level=q.popleft()
            if level>prelevel:
                prelevel=level
                prenum=num
            res=max(res, num - prenum +1 )
            if node.left:
                q.append([node.left,2*num,level+1])
            if node.right:
                q.append([node.right,2*num+1,level+1])
        return res