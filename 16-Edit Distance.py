class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dis=[[float('inf')]*(len(word1)+1) for _ in range((len(word2)+1))]
        for i in range(len(word1)+1):
            dis[len(word2)][i]=len(word1)-i
        for j in range(len(word2)+1):
            dis[j][len(word1)]=len(word2)-j
        for i in range(len(word2)-1,-1,-1):
            for j in range(len(word1)-1,-1,-1):
                if word1[j]==word2[i]:
                    dis[i][j]=dis[i+1][j+1]
                else:
                    dis[i][j]=1+min(dis[i][j+1],dis[i+1][j],dis[i+1][j+1])
        return dis[0][0]



'''SOLVED BY ADIT MUGDHA DAS'''