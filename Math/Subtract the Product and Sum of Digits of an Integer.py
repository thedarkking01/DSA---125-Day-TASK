# LeetCode Problem: Subtract the Product and Sum of Digits of an Integer
# Difficulty: Easy
# URL: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

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