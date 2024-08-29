# Platform = GFG
# link=https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        i,j=1,0
        platform_need=1
        max_platform=1
        while i<n and j<n:
            if arr[i]<=dep[j]:
                platform_need+=1
                
                i+=1
            else:
                platform_need-=1
                j+=1
        return max(platform_need,max_platform)
    
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

solution = Solution()
print("Minimum number of platforms required:", solution.minimumPlatform(n, arr, dep))
