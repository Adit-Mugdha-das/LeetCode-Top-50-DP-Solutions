class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def help(i):
            if i<0:
                return 0
            if i not in dp:
                dp[i]=max(nums[i]+help(i-2),help(i-1))
            return dp[i]
        return help(len(nums)-1)
    
'''SOLVED BY ADIT MUGDHA DAS'''