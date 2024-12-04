class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg=[],[]
        res=[]
        for n in nums:
            if n<0:
                neg.append(n)
            elif n>0:
                pos.append(n)
        for p,n in zip(pos,neg):
            res.append(p)
            res.append(n)
        return res