class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        depth=0
        for c in s:
            if c == '(':
                if depth > 0:
                    res.append(c)  
                depth += 1
            elif c == ')':
                depth -= 1
                if depth > 0:
                    res.append(c)
        return "".join(res)