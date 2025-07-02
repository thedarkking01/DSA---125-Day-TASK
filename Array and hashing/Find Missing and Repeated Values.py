class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        double = missing = 0
        for num in range(1, n * n + 1):
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if num == grid[i][j]:
                        cnt += 1
            if cnt == 2:
                double = num
            elif cnt == 0:
                missing = num

        return [double, missing]