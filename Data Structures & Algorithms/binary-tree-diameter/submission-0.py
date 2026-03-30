# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.result = 0    
        def maxDepth(root):
            if root is None:
                return 0
            right_depth = maxDepth(root.right)
            left_depth = maxDepth(root.left)
            maxdepth = 1 + max(right_depth, left_depth)
            if (left_depth + right_depth) > self.result:
                self.result = left_depth + right_depth
            return maxdepth
        maxDepth(root)
        return self.result

         

        