class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        maxside=0 
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    if i==0 or j==0:  
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxside=max(maxside,dp[i][j])
        return maxside*maxside

'''SOLVED BY ADIT  MUGDHA DAS'''