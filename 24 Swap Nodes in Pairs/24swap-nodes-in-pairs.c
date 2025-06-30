/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode *p;
    p=head;
    if(head==NULL || head->next==NULL) return head;
    while(head!=NULL && head->next!=NULL){
        int temp=head->val;
        head->val=head->next->val;
        head->next->val=temp;
        head=head->next->next;
    }
    return p;
}