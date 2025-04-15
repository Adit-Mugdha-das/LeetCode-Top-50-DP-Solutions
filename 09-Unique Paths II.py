class Solution:
    def __init__(self):
        self.dp=defaultdict(int)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        def unique(r,c):
            if (r,c) in self.dp:
                return self.dp[(r,c)]
            if r==m-1 and c==n-1 and obstacleGrid[r][c]!=1:
                return 1
            if r>=m or c>=n or obstacleGrid[r][c]==1 :
                return 0
            self.dp[(r,c)]=unique(r+1,c)+unique(r,c+1)
            return self.dp[(r,c)]
        return unique(0,0)
            
'''SOLVED BY ADIT MUGDHA DAS'''