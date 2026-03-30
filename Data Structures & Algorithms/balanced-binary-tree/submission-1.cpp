/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool result = true;
    int maxDepth(TreeNode* root){
        if(root == nullptr){
            return 0;
        }
        int right_depth = maxDepth(root->right);
        int left_depth = maxDepth(root->left);
        int maxdepth = 1 + max(right_depth,left_depth);
        if(abs(right_depth-left_depth) > 1){
            result = false;
        }
        return maxdepth;
    }
    bool isBalanced(TreeNode* root) {
        if (root == nullptr){
            return true;
        }
        maxDepth(root);

        return result;


        
    }
};
