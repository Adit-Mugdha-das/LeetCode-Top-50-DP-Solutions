class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        squares=[i*i for i in range(1,int(math.isqrt(n))+1)]
        for i in range(1,n+1):
            for sq in squares:
                if sq>i:
                    break
                dp[i]=min(dp[i],dp[i-sq]+1)
        return dp[n]

'''SOLVED BY ADIT MUGDHA DAS'''