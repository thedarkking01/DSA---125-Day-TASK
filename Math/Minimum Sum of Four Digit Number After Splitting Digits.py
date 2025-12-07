class Solution:
    def minimumSum(self, num: int) -> int:
        res = [0] * 4
        i = 0
        while num > 0:
            res[i] = num % 10
            num //= 10
            i += 1
        res.sort()
        return res[0] * 10 + res[2] + res[1] * 10 + res[3]