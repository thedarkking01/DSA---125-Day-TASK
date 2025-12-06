# leetcode 1175: Prime Arrangements
# Difficulty: Easy
# URL: https://leetcode.com/problems/prime-arrangements/
class Solution:
    mod = 10**9 + 7
    
    def numPrimeArrangements(self, n: int) -> int:
        def factorial(num):
            res = 1
            for i in range(2, num + 1):
                res = (res * i) % self.mod
            return res
        
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        total_prime = sum(1 for i in range(1, n + 1) if is_prime(i))
        non_prime = n - total_prime
        fact = (factorial(total_prime) * factorial(non_prime)) % self.mod
        return fact