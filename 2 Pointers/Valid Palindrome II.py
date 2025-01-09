class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalin(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        l,r=0,len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return ispalin(l+1,r) or ispalin(l,r-1)
        return True