class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n==0:
        #     return False
        # for x in range(31):
        #     if n==2**x:
        #         return True
        # return False

        if n == 0:
            return False
        while n > 0:
            if n == 1:
                return True
            if n % 2 != 0:
                break
            n //= 2
        return False