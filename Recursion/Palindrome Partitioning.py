class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def dfs(i, part):
            if i == len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if self.pali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1, part)
                    part.pop()

        dfs(0, [])
        return res

    def pali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True