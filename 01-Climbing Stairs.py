class Solution:
    def __init__(self):
        self.dp=defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        if n<=1:
            return 1
        self.dp[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.dp[n]
        
''''SOLVED BY ADIT MUGDHA DAS'''