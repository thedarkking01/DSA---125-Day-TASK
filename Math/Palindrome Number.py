# Problem Statement :

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Examples:

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
 

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Constraints: 
#   -231 <= x <= 231 - 1

#  Pseudocode:
    # Define a function isPalindrome that takes an integer x as input and returns a boolean.
    # Initialize variables n, rem, and rev to store the original value of x, the remainder, and the reversed number, respectively.
    # Start a while loop while n is not equal to 0:
    # Calculate the remainder of n when divided by 10 and store it in rem.
    # Multiply rev by 10 and add rem to rev.
    # Update n by dividing it by 10.
    # Check if the original number x is non-negative and if the reversed number rev is equal to x:
    # If true, return true, indicating that x is a palindrome.
    # If false, return false.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False 
        rev=0
        orig=x
        while x!=0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        return rev==orig