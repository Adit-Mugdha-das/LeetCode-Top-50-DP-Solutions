class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word=set(wordDict)
        dp=defaultdict(bool)
        dp[len(s)]=True
        def helper(i):
            if i in dp:
                return dp[i]
            for j in range(i,len(s)):
                if s[i:j+1] in word:
                    if helper(j+1):
                        dp[i]=True
                        return True
            dp[i]=False
            return dp[i]
        return helper(0)
        
'''SOLVED BY ADIT MUGDHA DAS'''