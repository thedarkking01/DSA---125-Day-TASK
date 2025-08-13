class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(start,current,total):
            # base case
            if total==target:
                res.append(list(current))
                return 
            # prune approach
            if total>target:
                return 
            
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                backtrack(i,current,total+candidates[i])
                current.pop()
        backtrack(0,[],0)
        return res