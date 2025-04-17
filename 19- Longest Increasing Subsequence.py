class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dis=[1]*n
        for i in range(n,-1,-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    dis[i]=max(dis[i],1+dis[j])
        return max(dis)
    
'''SOLVED BY ADIT MUGDHA DAS'''