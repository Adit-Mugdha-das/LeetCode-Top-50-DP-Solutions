class Solution:
    def numTilings(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 5
        num=[0]*(n+1)
        num[0]=1
        num[1]=1
        num[2]=2
        num[3]=5
        for i in range(4,n+1):
            num[i]=(2*num[i-1]+num[i-3])
        return num[n]%(10**9+7)

'''SOLVED BY ADIT MUGDHA DAS'''