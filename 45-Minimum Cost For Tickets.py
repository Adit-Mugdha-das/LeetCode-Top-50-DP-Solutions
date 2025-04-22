class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=max(days)
        set_day=set(days)
        dp=[0]*(n+1)
        for i in range(n+1):
            if i not in set_day:
                dp[i]=dp[i-1]
            else:
                dp[i]=min(costs[0]+dp[max(0,i-1)],costs[1]+dp[max(0,i-7)],costs[2]+dp[max(0,i-30)])
        return dp[n]

'''SOLVED BY ADIT MUGDHA DAS'''