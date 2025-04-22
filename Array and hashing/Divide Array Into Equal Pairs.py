class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        N = len(nums)
        nums.sort()
        i = 0
        while i < N:
            j = i
            while j < N and nums[i] == nums[j]:
                j += 1
            if (j - i) % 2 != 0:
                return False
            i = j
        return True