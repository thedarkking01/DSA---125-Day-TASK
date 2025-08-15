from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        l = 1  
        for r in range(1, n): 
            if nums[r] != nums[l - 1]:
                nums[l] = nums[r]
                l += 1
        return l