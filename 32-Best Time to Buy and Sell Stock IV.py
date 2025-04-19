class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k==0:
            return 0
        n=len(prices)
        if  k>=n//2:
            return sum(max(prices[i+1]-prices[i],0) for i in range(n-1))
        dp=[[0]*n for i in range(k+1)]
        for i in range(1,k+1):
            maxdif=-prices[0] 
            for j in range(1,n):
                dp[i][j]=max(dp[i][j-1],prices[j]+maxdif)
                maxdif = max(maxdif,dp[i-1][j]-prices[j])
        return dp[k][-1]

'''SOLVED BY ADIT MUGDHA DAS'''