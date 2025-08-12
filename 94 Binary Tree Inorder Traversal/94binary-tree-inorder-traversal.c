/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 int * inorder(struct TreeNode *t,int *arr,int *a){
    if(t!=NULL){
        inorder(t->left,arr,a);
        arr[(*a)++]=t->val;
        inorder(t->right,arr,a);
    }
    return arr;
 }
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize=0;
    int *result;
    result=(int *)malloc(100*sizeof(int));
    inorder(root,result,returnSize);
    return result;
}