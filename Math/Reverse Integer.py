# Problem Statement :

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Examples:
 

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321


# Constraints:  
# -231 <= x <= 231 - 1

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