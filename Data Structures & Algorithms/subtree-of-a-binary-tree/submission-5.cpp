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
    bool sameTree(TreeNode* a, TreeNode* b){
        if(!a && !b){
            return true;
        }else if(!a){
            return false;
        }else if(!b){
            return false;
        }
        if(a->val == b->val){
            return sameTree(a->left, b->left ) && sameTree(a->right, b->right);
        }
        return false;
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!root && !subRoot){
            return true;
        }else if(!root){
            return false;
        }else if(!subRoot){
            return false;
        }
        if(sameTree(root, subRoot)){
            return true;
        }else{
            return isSubtree(root->left , subRoot) ||  isSubtree(root->right , subRoot);
        }
    }
};
