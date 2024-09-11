class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value=set()
        l=0
        for r in range(len(nums)):
            if nums[r] in value:
                return True
            value.add(nums[r])
            if len(value)>k:
                value.remove(nums[r-k])
        return False