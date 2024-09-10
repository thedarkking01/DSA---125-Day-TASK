class Solution:
    def minInsertions(self, s: str) -> int:
        rev_str=s[::-1]
        n=len(s)
        dp=[[0]*(n+1) for i in range(n+1)] 
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==rev_str[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j]=max(dp[i - 1][j], dp[i][j - 1])
        length=dp[n][n]
        return n - length