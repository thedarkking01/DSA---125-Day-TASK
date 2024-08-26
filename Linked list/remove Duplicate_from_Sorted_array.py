class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                r+=1
            l+=1
        return l