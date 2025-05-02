class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        seen=set()
        for n in nums:
            if n in seen:
                res.append(n)
            else:
                seen.add(n)
        return res