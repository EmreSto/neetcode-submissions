# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.result = True
        def maxDepth(root):
            if root is None:
                return 0
            right_depth = maxDepth(root.right)
            left_depth = maxDepth(root.left)
            maxdepth = 1 +max(right_depth, left_depth)
            if abs(left_depth - right_depth) > 1:
                self.result = False
            return maxdepth
        maxDepth(root)
        return self.result


    

    
        
        