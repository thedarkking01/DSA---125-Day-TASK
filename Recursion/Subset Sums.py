#problem link =https://www.geeksforgeeks.org/problems/subset-sums2234/1
#GFG problem

class Solution:
	def subsetSums(self, arr, n):
		res=[]
		def dfs(i,cursum=0):
			if i==n:
                res.append(cursum)
                return
            dfs(i+1,cursum)
            dfs(i+1,cursum+arr[i])
	    dfs(0)
	    return res

solution = Solution()
arr = [2, 3]
n = len(arr)
print(solution.subsetSums(arr, n))