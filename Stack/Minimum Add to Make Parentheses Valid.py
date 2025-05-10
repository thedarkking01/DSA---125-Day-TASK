class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened=closed=0
        for c in s:
            if c == "(":
                closed+=1
            elif c==")":
                if closed>0:
                    closed-=1
                else:
                    opened+=1
        return opened+closed