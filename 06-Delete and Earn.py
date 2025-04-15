class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        c=Counter(nums)
        mnum=max(nums)
        dp=[0]*(mnum+1)
        dp[1]=c[1]*1
        for i in range(2,mnum+1):
            dp[i]=max(dp[i-1], dp[i-2]+i*c[i])
        return dp[mnum]

'''SOLVED BY ADIT MUGDHA DAS'''