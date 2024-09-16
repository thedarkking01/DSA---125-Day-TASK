class Solution:
    def get_next(self, n: int) -> int:
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum += digit ** 2
            n //= 10
        return total_sum

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)   
            fast = self.get_next(self.get_next(fast))  
        return fast == 1