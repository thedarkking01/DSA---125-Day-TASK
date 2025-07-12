class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)
        res=[]
        for num in set1:
            if num in set2:
                res.append(num)
        return res