# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def traversal_recursion(preorder,inorder):
            if not preorder:
                return None
            root_val = preorder[0]
            mid = inorder.index(root_val)
            left_subtree_inorder = inorder[0 : mid]
            right_subtree_inorder = inorder[mid+1 : ]
            L = len(left_subtree_inorder)
            left_subtree_preorder = preorder[1 : 1 +L]
            right_subtree_preorder = preorder[1 + L: ]
            node = TreeNode(root_val)
            node.left = traversal_recursion(left_subtree_preorder,left_subtree_inorder)
            node.right = traversal_recursion(right_subtree_preorder,right_subtree_inorder)
            return node
        return traversal_recursion(preorder,inorder)



