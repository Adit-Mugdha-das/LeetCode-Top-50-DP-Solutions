class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i]=1 
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j]=2+dp[i+1][j-1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        lps=dp[0][n-1]
        return n-lps

'''SOLVED BY ADIT MUGDHA DAS'''