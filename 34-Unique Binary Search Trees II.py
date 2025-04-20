# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []
        def generate(st,end):
            if st>end:
                return [None]
            trees=[]
            for i in range(st,end+1):
                ltrees=generate(st,i-1)
                rtrees=generate(i+1,end)
                for l in ltrees:
                    for r in rtrees:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        trees.append(root)
            return trees
        return generate(1,n)
    

'''SOLVED BY ADIT MUGDHA DAS'''