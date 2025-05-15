"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def helper(root):
            if not root:
                return 
            for c in root.children:
                helper(c)
            res.append(root.val)
        helper(root)
        return res 