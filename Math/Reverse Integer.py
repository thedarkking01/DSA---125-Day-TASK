class Solution:
    def reverse(self, x: int) -> int:
        rem=rev=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x!=0:
            rem=x%10
            rev=rev*10+rem
            x=x//10

        if rev < -2**31 or rev > 2**31:
            return 0
        return sign*rev