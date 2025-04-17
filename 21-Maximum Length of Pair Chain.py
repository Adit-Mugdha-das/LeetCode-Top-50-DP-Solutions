class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n=len(pairs)-1
        dis=[1]*(n+1)
        for i,(u,v) in enumerate(reversed(pairs)):
            for j in range(n-i+1,n+1):
                if pairs[j][0]>v:
                    dis[n-i]=max(dis[n-i],1+dis[j])
        return max(dis)


'''SOLVED BY ADIT MUGDHA DAS'''