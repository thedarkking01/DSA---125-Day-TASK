class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cursum=sum(arr[:k])
        res=0
        if cursum>=threshold*k:
            res+=1
        for i in range(k,len(arr)):
            cursum+=arr[i]-arr[i-k]
            if cursum>=threshold*k:
                res+=1
        return res