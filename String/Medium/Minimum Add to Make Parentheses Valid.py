class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openn=closed=0
        for c in s:
            if c=='(':
                closed+=1
            elif c==')':
                if closed>0:
                    closed-=1
                else:
                    openn+=1
        return openn+closed