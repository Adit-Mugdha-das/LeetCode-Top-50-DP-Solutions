class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[defaultdict(int) for i in range(n)]
        mln=0
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]=dp[j][diff]+1 if diff in dp[j] else 2
                mln=max(mln,dp[i][diff])
        return mln

'''SOLVED BY ADIT MUGDHA DAS'''