# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs (node, max_so_far):
            if node is None:
                return 0 
            count =0
            if node.val >= max_so_far:
                count +=1
            a =dfs(node.right, max(node.val,max_so_far))
            b =dfs(node.left, max(node.val,max_so_far))
            count = count + a + b
            return count
        return dfs(root, root.val)

        