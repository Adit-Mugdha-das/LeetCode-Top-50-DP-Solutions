class Solution:
    def __init__(self):
        self.dp=defaultdict(int) 
    def fib(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        if n==0:
            return 0
        if n<=2:
            return 1
        self.dp[n]=self.fib(n-1)+self.fib(n-2)
        return self.dp[n]

'''SOLVED BY ADIT MUGDHA DAS'''