class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n=len(cost)
        if n==0:
            return 0
        if n==1:
            return cost[1]
        prev=cost[0]
        prev2=cost[1]
        for i in range(2,n):
            cur=cost[i]+min(prev,prev2)
            prev,prev2=prev2,cur
        return min(prev,prev2)

'''SOLVED BY ADIT MUGDHA DAS'''