class Solution:
    MOD= 10**9 + 7
    @staticmethod
    def power(x, n):
        if n == 0:
            return 1
        half = Solution.power(x, n // 2)
        result = (half * half) % Solution.MOD
        if n % 2 == 0:
            return result
        else:
            return (result * x) % Solution.MOD
    
    def count_good_numbers(self, n: int) -> int:
        even_count = (n + 1) // 2
        odd_count = n // 2
        return (self.power(5, even_count) * self.power(4, odd_count)) % self.MOD