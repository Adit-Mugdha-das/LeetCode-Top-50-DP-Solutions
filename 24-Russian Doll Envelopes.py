class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        heights=[h for _,h in envelopes]
        dp=[]
        for h in heights:
            i=bisect.bisect_left(dp,h)
            if i<len(dp):
                dp[i]=h
            else:
                dp.append(h)
        return len(dp)

'''SOLVED BY ADIT MUGDHA DAS'''