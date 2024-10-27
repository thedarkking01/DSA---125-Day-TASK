class Solution:
    def check(self, nums: List[int]) -> bool:
        count_break=0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                count_break+=1
        return count_break<=1