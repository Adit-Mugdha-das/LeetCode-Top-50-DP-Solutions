class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0 and i-coin<=amount:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1

'''SOLVED BY ADIT MUGDHA DAS'''