class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=max1=0
        for n in nums:
            if n==1:
                max1+=1
                res=max(res,max1)
            else:
                max1=0
        return res