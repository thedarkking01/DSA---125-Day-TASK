class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftsum=0
        for i in range(len(nums)):
            rightsum=total-nums[i]-leftsum
            if rightsum==leftsum:
                return i
            leftsum+=nums[i]
        return -1