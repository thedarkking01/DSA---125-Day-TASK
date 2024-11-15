class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def cal_sum(d):
            return sum(math.ceil(n / d) for n in nums)
        
        l,r=1,max(nums)
        res=r
        while l<=r:
            m=(l+r)//2
            if cal_sum(m)<=threshold:
                res=m
                r = m - 1
            else:
                l=m+1
        return res