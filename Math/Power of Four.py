# 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(31):
            if i**4==n:
                return True
        return False

# Bit Mask - II
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n % 3 == 1)