class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        # swap adjacent elements
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums        