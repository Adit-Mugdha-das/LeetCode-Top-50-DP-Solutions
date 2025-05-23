# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0,0)
            left=dfs(node.left)
            right=dfs(node.right)
            rob=node.val+left[1]+right[1]
            skip=max(left)+max(right)
            return (rob,skip)
        return max(dfs(root))
    
'''SOLVED BY ADIT MUGDHA DAS'''