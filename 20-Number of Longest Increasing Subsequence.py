class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dis=[1]*n
        count=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    if dis[j]+1>dis[i]:
                        dis[i]=dis[j]+1
                        count[i]=count[j]
                    elif dis[j]+1==dis[i]:
                        count[i]+=count[j]
        max_num=max(dis)
        return sum(count[i] for i in range(n) if dis[i]==max_num)
    
'''SOLVED BY ADIT MUGDHA DAS'''