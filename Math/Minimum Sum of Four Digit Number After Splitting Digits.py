# url : https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
# difficulty : Easy

class Solution:
    def minimumSum(self, num: int) -> int:
        result = [0] * 4
        i = 0
        while num > 0:
            result[i] = num % 10
            num //= 10
            i += 1
        result.sort()
        return result[0] * 10 + result[2] + result[1] * 10 + result[3]