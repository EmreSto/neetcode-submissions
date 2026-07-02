# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       queue = deque([root])
       result = []
       if not root:
        return []
       while len(queue) != 0:
        level_values = []
        qsize = len(queue)
        for i in range(qsize):
            a = queue.popleft()
            level_values.append(a.val)
            if a.left != None:
                queue.append(a.left)
            if a.right != None:
                queue.append(a.right)
        result.append(level_values)
       return result
    


            
