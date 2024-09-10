# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp=[0]*len(text1)
#         longest=0
#         for c in text2:
#             curlen=0
#             for i,val in enumerate(dp):
#                 if curlen<val:
#                     curlen=val
#                 elif c==text1[i]:
#                     dp[i]=curlen+1
#                     longest=max(longest,curlen+1)
#         return longest

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[0] * (n + 1) for i in range(m + 1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[m][n]