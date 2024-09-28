class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        def dfs(i,j):
            if i>=len(grid) or j>=len(grid[i]) or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            preim=dfs(i+1,j)
            preim+=dfs(i,j+1)
            preim+=dfs(i,j-1)
            preim+=dfs(i-1,j)
            return preim
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)