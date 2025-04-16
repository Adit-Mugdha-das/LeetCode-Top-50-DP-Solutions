class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dis=[[0]*(len(s1)+1) for _ in range(len(s2)+1)]
        for i in range(len(s1)-1,-1,-1):
            dis[len(s2)][i]=dis[len(s2)][i+1]+ord(s1[i])
        for j in range(len(s2)-1,-1,-1):
            dis[j][len(s1)]=dis[j+1][len(s1)]+ord(s2[j])
        for i in range(len(s2)-1,-1,-1):
            for j in range(len(s1)-1,-1,-1):
                if s1[j]==s2[i]:
                    dis[i][j]=dis[i+1][j+1]
                else:
                    dis[i][j]=min(dis[i+1][j]+ord(s2[i]),dis[i][j+1]+ord(s1[j]))
        return dis[0][0] 
    
'''SOLVED BY ADIT MUGDHA DAS'''