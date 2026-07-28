# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            l_s = dfs(node.left)
            r_s = dfs(node.right)

            self.ans+=abs(l_s-r_s)
            return l_s+r_s+node.val
        dfs(root)
        return self.ans