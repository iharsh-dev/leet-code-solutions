/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode *p=head;
    int arr[k];
    while(p!=NULL){
        struct ListNode *current;
        current=p;
        for(int i=0;i<k-1;i++){
            if(p->next==NULL){
                return head;
            }
            else p=p->next;
        }
        p=current;
        for(int i=0;i<k;i++){
            arr[i]=p->val;
            p=p->next;
        }
        p=current;
        for(int i=k-1;i>=0;i--){
            p->val=arr[i];
            p=p->next;
        }

    }
    return head;
}