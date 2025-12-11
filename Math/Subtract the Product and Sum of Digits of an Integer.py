# LeetCode Problem: Subtract the Product and Sum of Digits of an Integer
# Difficulty: Easy
# URL: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

# Problem Statement :

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.


# Examples:
 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
 

# Example 2:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15



# Constraints : 
# 1 <= n <= 10^5



#    Pseudocode:
    # Define a function subtractProductAndSum that takes an integer n as input and returns an integer.
    # Initialize variables sum and prod to 0 and 1 respectively.
    # Initialize variable num to 0.
    # Start a while loop while n is greater than 0:
    # Calculate the last digit of n and store it in num.
    # Update prod by multiplying it with num.
    # Update sum by adding num to it.
    # Divide n by 10 to remove the last digit.
    # Calculate the difference between prod and sum.
    # Return the difference.



class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_val = 0
        prod = 1
        while n > 0:
            num = n % 10
            prod *= num
            sum_val += num
            n //= 10
        return prod - sum_val