class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth=0
        depth=0
        for c in s:
            if c == '(':  
                depth += 1
                maxdepth = max(maxdepth, depth)
            elif c == ')':
                depth -= 1
        return maxdepth