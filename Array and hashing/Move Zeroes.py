class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(0,len(nums)):
            if nums[r]==0:
                r+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1