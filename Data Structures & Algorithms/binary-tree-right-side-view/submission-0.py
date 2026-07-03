# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])
        if not root:
            return []
        while len(queue) != 0:
            qsize = len(queue)
            for i in range(qsize):
                a = queue.popleft()
                if a.left != None:
                    queue.append(a.left)
                if a.right != None:
                    queue.append(a.right)
                if (i == qsize-1):
                    result.append(a.val)
        return result

                
                
            
        