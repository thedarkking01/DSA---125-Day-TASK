# brute force solution

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            flag=True
            for j in range(len(arr)):
                if i==j:
                    continue
                if arr[i]==arr[j]:
                    flag=False
                    break
            if flag:
                k-=1
                if k==0:
                    return arr[i]
        return ""