
# Problem Statement :

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.
# Examples:

# Example 1:

# Input: n = 16
# Output: true
 

# Example 2:

# Input: n = 5
# Output: false

# Constraints:
# 2^31 <= n <= 2^31 - 1



#    Pseudocode:
        # Define a function isPowerofFour that takes an integer n as input and returns a boolean.
        # Check if the expression (n & (n - 1)) == 0 is true:
        # This condition checks if n is a power of 2, meaning it has only one bit set. If it's true, it indicates that n is a power of 2.
        # Check if the expression n % 3 == 1 is true:
        # This condition checks if n modulo 3 is equal to 1. If it's true, it indicates that n is in the form 4k.
        # Return the result of the logical AND operation between the results of the two conditions in step 2 and step 3. If both conditions are true, it indicates that n is a power of 4


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