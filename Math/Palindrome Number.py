# Problem Statement :

# Given an integer x, return true if x is a palindrome, and false otherwise.

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