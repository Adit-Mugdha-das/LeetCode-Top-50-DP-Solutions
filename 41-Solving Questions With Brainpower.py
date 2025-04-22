class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):  
            pts,skip =questions[i]
            nextq=i+skip+1
            sol=pts+(dp[nextq] if nextq<n else 0)
            skipq=dp[i+1]
            dp[i]=max(sol,skipq)
        return dp[0]

'''SOLVED BY ADIT MUGDHA DAS'''