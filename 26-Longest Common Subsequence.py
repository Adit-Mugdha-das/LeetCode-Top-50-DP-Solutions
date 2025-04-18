class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dis=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dis[i][j]=1+dis[i+1][j+1]
                else:
                    dis[i][j]=max(dis[i][j+1],dis[i+1][j])
        return dis[0][0]
'''SOLVED BY ADIT MUGDHA DAS'''