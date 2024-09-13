class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,res,total=0,0,0
        for r in range(len(s)):
            if s[r] in 'aeiou':
                total+=1
            if r>=k:
                if s[l] in 'aeiou':
                    total-=1
                l+=1
            if r>=k-1:
                res=max(res,total)
        return res