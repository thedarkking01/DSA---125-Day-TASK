class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(c.lower() for c in s if c.isalnum())
        l,r=0,len(s)-1
        # s=s.isalnum()
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True