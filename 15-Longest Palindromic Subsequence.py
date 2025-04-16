class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp={}
        def helper(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if (i,j)in dp:
                return dp[(i,j)]
            if s[i]==s[j]:
                dp[(i,j)]=2+helper(i+1,j-1)
            else:
                dp[(i,j)]=max(helper(i+1,j),helper(i,j-1))
            return dp[(i,j)]
        return helper(0,len(s)-1)
            

'''SOLVED BY ADIT MUGDHA DAS'''