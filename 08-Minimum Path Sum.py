class Solution:
    def __init__(self):
        self.dp=defaultdict(int)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def minsum(r,c):
            if (r,c) in self.dp:
                return self.dp[(r,c)]
            if r==m-1 and c==n-1:
                return grid[r][c]
            if r>=m or c>=n:
                return float('inf')
            self.dp[(r,c)]=grid[r][c]+min(minsum(r+1,c),minsum(r,c+1))
            return self.dp[(r,c)]
        return minsum(0,0)
        
'''SOLVED BY ADIT MUGDHA DAS'''