# Problem Statement :

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well. You must not use any built-in exponent function or operator.



# Examples:
# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


# Constraints: 
# 0 <= x <= 231 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        res=0
        while l<=r:
            m=(l+r)//2
            if m**2>x:
                r=m-1
            elif m**2<x:
                l=m+1
                res=m
            else:
                return m
        return res