class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1,set2=set(nums1),set(nums2)
        l1=[n for n in set1 if n not in set2]
        l2=[n for n in set2 if n not in set1]
        return [l1,l2]